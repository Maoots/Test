"""DALL-E 3 image generation."""

import os
import pathlib
import urllib.request
from datetime import datetime

from openai import OpenAI

from . import config
from .prompts import build_prompt


def generate_image(prompt: str | None = None) -> tuple[str, str, bytes]:
    """
    Generate one garden image.

    Returns:
        (prompt_used, local_file_path, image_bytes)
    """
    client = OpenAI(api_key=config.OPENAI_API_KEY)

    if prompt is None:
        prompt = build_prompt()

    print(f"[generator] Prompt:\n  {prompt[:120]}...")

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="hd",
        style="natural",
        n=1,
    )

    image_url = response.data[0].url
    revised_prompt = response.data[0].revised_prompt or prompt

    print(f"[generator] Image URL received (expires ~1h)")

    image_bytes = _download(image_url)

    local_path = _save_locally(image_bytes)
    print(f"[generator] Saved locally: {local_path}")

    return revised_prompt, local_path, image_bytes


def _download(url: str) -> bytes:
    with urllib.request.urlopen(url) as response:
        return response.read()


def _save_locally(image_bytes: bytes) -> str:
    images_dir = pathlib.Path(config.IMAGES_DIR)
    images_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = images_dir / f"garden_{timestamp}.png"

    file_path.write_bytes(image_bytes)
    return str(file_path)

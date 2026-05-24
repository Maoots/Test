"""
Upload generated images to imgbb for a permanent public URL.

Instagram Graph API requires a publicly accessible image URL
(DALL-E 3 URLs expire in ~1 hour, so we re-host on imgbb).

imgbb free plan: unlimited uploads, images hosted indefinitely.
Sign up at https://imgbb.com and get an API key from https://api.imgbb.com
"""

import base64

import httpx

from . import config


def upload_image(image_bytes: bytes) -> str:
    """Upload image bytes to imgbb and return the permanent public URL."""
    encoded = base64.b64encode(image_bytes).decode("utf-8")

    response = httpx.post(
        "https://api.imgbb.com/1/upload",
        data={
            "key": config.IMGBB_API_KEY,
            "image": encoded,
            "expiration": 0,  # 0 = keep forever
        },
        timeout=60,
    )
    response.raise_for_status()

    data = response.json()
    if not data.get("success"):
        raise RuntimeError(f"imgbb upload failed: {data}")

    url = data["data"]["url"]
    print(f"[storage] Uploaded to imgbb: {url}")
    return url

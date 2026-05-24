"""Simple JSON log of all posts."""

import json
import pathlib
from datetime import datetime

from . import config


def record_post(prompt: str, local_path: str, image_url: str, media_id: str) -> None:
    log_path = pathlib.Path(config.LOG_FILE)

    entries: list = []
    if log_path.exists():
        entries = json.loads(log_path.read_text())

    entries.append(
        {
            "timestamp": datetime.now().isoformat(),
            "media_id": media_id,
            "local_file": local_path,
            "hosted_url": image_url,
            "prompt": prompt,
        }
    )

    log_path.write_text(json.dumps(entries, indent=2, ensure_ascii=False))
    print(f"[logger] Entry saved to {log_path}")


def last_post_date() -> str | None:
    log_path = pathlib.Path(config.LOG_FILE)
    if not log_path.exists():
        return None
    entries = json.loads(log_path.read_text())
    if not entries:
        return None
    return entries[-1]["timestamp"][:10]

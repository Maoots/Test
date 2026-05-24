"""Daily scheduler — runs the full post pipeline once per day at the configured time."""

import time
from datetime import datetime

import schedule

from . import config, logger
from .captions import build_caption
from .generator import generate_image
from .instagram import post_image
from .storage import upload_image


def run_daily_post() -> None:
    today = datetime.now(config.TIMEZONE).date().isoformat()

    last = logger.last_post_date()
    if last == today:
        print(f"[scheduler] Already posted today ({today}). Skipping.")
        return

    print(f"[scheduler] Starting daily post for {today}...")

    prompt, local_path, image_bytes = generate_image()
    public_url = upload_image(image_bytes)
    caption = build_caption()
    media_id = post_image(public_url, caption)

    logger.record_post(prompt, local_path, public_url, media_id)
    print(f"[scheduler] Done. Post published at {datetime.now(config.TIMEZONE).isoformat()}")


def start(post_time: str | None = None) -> None:
    """Start the scheduler. Blocks indefinitely."""
    target_time = post_time or config.POST_TIME
    print(f"[scheduler] Scheduled to post daily at {target_time} ({config.TIMEZONE})")

    schedule.every().day.at(target_time).do(run_daily_post)

    while True:
        schedule.run_pending()
        time.sleep(30)

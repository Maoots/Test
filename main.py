#!/usr/bin/env python3
"""
Garden Instagram Bot — CLI entry point.

Usage:
    python main.py post        # Generate and post immediately (one-shot)
    python main.py schedule    # Start the daily scheduler (blocking)
    python main.py preview     # Print a sample prompt without posting
    python main.py status      # Show the last post from the log
"""

import argparse
import json
import pathlib
import sys


def cmd_post() -> None:
    from garden_bot.captions import build_caption
    from garden_bot.generator import generate_image
    from garden_bot.instagram import post_image
    from garden_bot import logger
    from garden_bot.storage import upload_image

    prompt, local_path, image_bytes = generate_image()
    public_url = upload_image(image_bytes)
    caption = build_caption()

    print("\n── Caption preview ──────────────────────────")
    print(caption[:300])
    print("─────────────────────────────────────────────\n")

    media_id = post_image(public_url, caption)
    logger.record_post(prompt, local_path, public_url, media_id)
    print(f"\nPosted successfully! Media ID: {media_id}")


def cmd_schedule(args: argparse.Namespace) -> None:
    from garden_bot.scheduler import start
    start(post_time=args.time)


def cmd_preview() -> None:
    from garden_bot.prompts import build_prompt
    from garden_bot.captions import build_caption

    print("\n── Prompt ───────────────────────────────────")
    print(build_prompt())
    print("\n── Caption ──────────────────────────────────")
    print(build_caption())
    print("─────────────────────────────────────────────\n")


def cmd_status() -> None:
    from garden_bot import config
    log_path = pathlib.Path(config.LOG_FILE)
    if not log_path.exists():
        print("No posts yet.")
        return
    entries = json.loads(log_path.read_text())
    if not entries:
        print("Log file is empty.")
        return
    last = entries[-1]
    print(f"\nTotal posts:   {len(entries)}")
    print(f"Last post:     {last['timestamp']}")
    print(f"Media ID:      {last['media_id']}")
    print(f"Local file:    {last['local_file']}")
    print(f"Hosted URL:    {last['hosted_url']}")
    print(f"Prompt start:  {last['prompt'][:100]}...")


def main() -> None:
    parser = argparse.ArgumentParser(description="Garden Instagram Bot")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("post", help="Generate and post one image now")

    sched = sub.add_parser("schedule", help="Start the daily scheduler")
    sched.add_argument("--time", default=None, help="Post time HH:MM (default from .env)")

    sub.add_parser("preview", help="Preview a prompt and caption without posting")
    sub.add_parser("status", help="Show last post info")

    args = parser.parse_args()

    if args.command == "post":
        cmd_post()
    elif args.command == "schedule":
        cmd_schedule(args)
    elif args.command == "preview":
        cmd_preview()
    elif args.command == "status":
        cmd_status()
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

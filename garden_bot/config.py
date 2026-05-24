import os
from zoneinfo import ZoneInfo

from dotenv import load_dotenv

load_dotenv()


def _require(key: str) -> str:
    value = os.environ.get(key)
    if not value:
        raise EnvironmentError(f"Missing required env var: {key}")
    return value


OPENAI_API_KEY: str = _require("OPENAI_API_KEY")
INSTAGRAM_USER_ID: str = _require("INSTAGRAM_USER_ID")
INSTAGRAM_ACCESS_TOKEN: str = _require("INSTAGRAM_ACCESS_TOKEN")
IMGBB_API_KEY: str = _require("IMGBB_API_KEY")

POST_TIME: str = os.environ.get("POST_TIME", "09:00")
TIMEZONE: ZoneInfo = ZoneInfo(os.environ.get("TIMEZONE", "Europe/Paris"))

LOG_FILE: str = os.environ.get("LOG_FILE", "posts_log.json")
IMAGES_DIR: str = os.environ.get("IMAGES_DIR", "generated_images")

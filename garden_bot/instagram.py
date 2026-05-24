"""
Instagram Graph API integration.

Requires:
  - A Facebook Page linked to an Instagram Business/Creator account
  - A long-lived access token with instagram_basic,
    instagram_content_publish, and pages_read_engagement permissions
  - The Instagram User ID (not the username — the numeric ID)

Flow:
  1. Create a media container with the image URL → get container_id
  2. Publish the container → get media_id
"""

import time

import httpx

from . import config

GRAPH_BASE = "https://graph.facebook.com/v19.0"


def post_image(public_image_url: str, caption: str) -> str:
    """
    Post an image to Instagram.

    Returns the published media ID.
    """
    container_id = _create_container(public_image_url, caption)

    # Instagram recommends waiting a few seconds before publishing
    time.sleep(5)

    media_id = _publish_container(container_id)
    print(f"[instagram] Published successfully. Media ID: {media_id}")
    return media_id


def _create_container(image_url: str, caption: str) -> str:
    url = f"{GRAPH_BASE}/{config.INSTAGRAM_USER_ID}/media"

    response = httpx.post(
        url,
        data={
            "image_url": image_url,
            "caption": caption,
            "access_token": config.INSTAGRAM_ACCESS_TOKEN,
        },
        timeout=60,
    )

    _check_response(response, "create media container")
    container_id = response.json()["id"]
    print(f"[instagram] Container created: {container_id}")
    return container_id


def _publish_container(container_id: str) -> str:
    url = f"{GRAPH_BASE}/{config.INSTAGRAM_USER_ID}/media_publish"

    response = httpx.post(
        url,
        data={
            "creation_id": container_id,
            "access_token": config.INSTAGRAM_ACCESS_TOKEN,
        },
        timeout=60,
    )

    _check_response(response, "publish container")
    return response.json()["id"]


def _check_response(response: httpx.Response, action: str) -> None:
    if response.status_code != 200 or "error" in response.json():
        raise RuntimeError(
            f"Instagram API error during {action}: "
            f"HTTP {response.status_code} — {response.text}"
        )

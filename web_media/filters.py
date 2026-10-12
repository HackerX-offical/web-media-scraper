from __future__ import annotations

from urllib.parse import urlparse

from web_media.extensions import DEFAULT_EXCLUDE_PATTERNS, IMAGE_EXTENSIONS, VIDEO_EXTENSIONS


def should_exclude_url(url: str, patterns: frozenset[str] = DEFAULT_EXCLUDE_PATTERNS) -> bool:
    if not url:
        return True
    lower = url.lower()
    return any(p in lower for p in patterns)


def is_media_path(path: str, image_ext: set[str] | None = None, video_ext: set[str] | None = None) -> bool:
    image_ext = image_ext or IMAGE_EXTENSIONS
    video_ext = video_ext or VIDEO_EXTENSIONS
    path_lower = path.lower()
    return any(path_lower.endswith(ext) for ext in image_ext | video_ext)

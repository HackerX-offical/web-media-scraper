from __future__ import annotations

import re
from urllib.parse import urljoin, urlparse

from web_media.extensions import IMAGE_EXTENSIONS, VIDEO_EXTENSIONS
from web_media.filters import is_media_path


def normalize_media_url(url: str, base_url: str) -> str:
    if not url or url.startswith(('data:', 'blob:', 'javascript:')):
        return ""
    url = url.split('#')[0]
    if not url.startswith(('http://', 'https://')):
        url = urljoin(base_url, url)
    return url


def is_media_url(url: str) -> bool:
    if not url:
        return False
    parsed = urlparse(url)
    if is_media_path(parsed.path.lower()):
        return True
    media_patterns = [
        r'/image/', r'/img/', r'/photo/', r'/picture/',
        r'/video/', r'/watch/', r'/stream/', r'/media/',
        'cloudflare', 'cdn', 'assets',
    ]
    lower = url.lower()
    return any(p in parsed.path.lower() or p in lower for p in media_patterns)

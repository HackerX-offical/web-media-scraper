"""Pure helpers for web media scraping (testable without network)."""

from web_media.paths import next_available_media_folder
from web_media.url_utils import is_media_url, normalize_media_url

__all__ = ['next_available_media_folder', 'normalize_media_url', 'is_media_url']

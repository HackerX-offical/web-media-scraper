from web_media.url_utils import is_media_url, normalize_media_url


def test_normalize_relative_to_absolute():
    url = normalize_media_url("/img/a.png", "https://example.com/page")
    assert url == "https://example.com/img/a.png"


def test_is_media_url_detects_video_path():
    assert is_media_url("https://example.com/videos/intro.mp4") is True

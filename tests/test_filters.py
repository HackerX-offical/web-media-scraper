from web_media.filters import is_media_path, should_exclude_url


def test_should_exclude_social_icons():
    assert should_exclude_url("https://cdn.example.com/logo.png") is True
    assert should_exclude_url("https://cdn.example.com/photo-hero.jpg") is False


def test_is_media_path_by_extension():
    assert is_media_path("/files/clip.webm") is True
    assert is_media_path("/files/readme.txt") is False

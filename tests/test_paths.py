from pathlib import Path

from web_media.paths import next_available_media_folder


def test_next_available_media_folder_starts_at_media(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    folder = next_available_media_folder()
    assert folder == Path("media")

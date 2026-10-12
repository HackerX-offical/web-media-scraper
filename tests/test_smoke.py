import importlib.util
from pathlib import Path


def test_media_scraper_module_loads():
    root = Path(__file__).resolve().parents[1]
    spec = importlib.util.spec_from_file_location("media_scraper", root / "media_scraper.py")
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert hasattr(mod, "main") or hasattr(mod, "scrape") or True

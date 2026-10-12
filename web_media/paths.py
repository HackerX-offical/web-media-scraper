from pathlib import Path


def next_available_media_folder(prefix: str = "media") -> Path:
    counter = 0
    while True:
        folder_name = prefix if counter == 0 else f"{prefix}-{counter}"
        folder_path = Path(folder_name)
        markdown_path = Path(f"{folder_name}_links.md")
        if not folder_path.exists() and not markdown_path.exists():
            return folder_path
        counter += 1

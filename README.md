# Web Media Scraper

A Python tool to scrape images and videos from any URL and generate a markdown file with media links. Features smart filtering to exclude UI elements and social media icons.

**Project**: [web-media-scraper](https://github.com/HackerX-offical/web-media-scraper)  
**Organization**: [HackerX](https://github.com/HackerX-offical)

## Installation

```bash
# Clone the repository
git clone https://github.com/HackerX-offical/web-media-scraper.git
cd web-media-scraper

# Run setup (creates virtual environment and installs dependencies)
./setup.sh
```

## Usage

```bash
# Run the scraper
./run.sh
```

The script will prompt for a URL and automatically download all media to the `media/` folder, generating `media_links.md` with organized links.

## Features

- **Smart Filtering**: Excludes social media icons and UI elements
- **Cloudflare Support**: Bypasses protection automatically
- **Multiple Sources**: Images, videos, background images, meta tags
- **Professional Output**: Clean markdown with statistics

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

**HackerX Organization** - Open Source Cybersecurity Tools

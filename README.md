# web-media-scraper

Python scraper that downloads page media and builds a markdown index.

## Why this exists

Authorized web archiving needs filtered image/video extraction without UI chrome. This tool outputs assets plus `media_links.md`.

## Features

- Cloudflare-aware fetching
- Filters social icons and chrome
- `setup.sh` / `run.sh` wrappers

## Install

```bash
git clone https://github.com/HackerX-official/web-media-scraper.git
cd web-media-scraper
./setup.sh
```

## Quick start

```bash
./run.sh
```

## Output

`media/` downloads and `media_links.md` with statistics.

## Develop

```bash
pytest tests -q
```

## Architecture

See [ARCHITECTURE.md](./ARCHITECTURE.md) for module layout and extension points.

## Ethics

Use only on systems and content you are **authorized** to test. See [SECURITY.md](./SECURITY.md).

## License

Licensed under the [HackerX License](./LICENSE). Redistributions must retain copyright,
license text, and [NOTICE](./NOTICE) attribution per the license terms.

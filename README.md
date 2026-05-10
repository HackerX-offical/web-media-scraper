# Web Media Scraper

<div align="center">

```
██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ██╗  ██╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗╚██╗██╔╝
███████║███████║██║     █████╔╝ █████╗  ██████╔╝ ╚███╔╝ 
██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗ ██╔██╗ 
██║  ██║██║  ██║╚██████╗██║  ██║███████╗██║  ██║██╔╝ ██╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
```

**OPEN SOURCE CYBERSECURITY & HACKING ORGANIZATION**

A powerful Python tool to scrape all images and videos from any URL and generate a comprehensive markdown file with media links. Features intelligent filtering to exclude UI elements and social media icons.

**Project**: [web-media-scraper](https://github.com/HackerX-offical/web-media-scraper)  
**Organization**: [HackerX](https://github.com/HackerX-offical)  
**Founder**: [Suryanshu Nabheet](https://github.com/HackerX-offical)

</div>

## Features

- **Comprehensive Media Detection**: Extracts images and videos from multiple sources:
  - Direct `<img>` and `<video>` tags
  - Picture tags with source sets
  - CSS background images
  - Open Graph and Twitter Card meta tags
  - YouTube/Vimeo embeds
  - Lazy-loaded images (data-src attributes)

- **Smart Filtering**: Automatically excludes:
  - Social media icons (Facebook, Twitter, Instagram, GitHub, etc.)
  - UI elements (logos, favicons, buttons, arrows)
  - Small spacer/pixel images
  - Navigation and header elements

- **Cloudflare Support**: Bypasses Cloudflare protection using cloudscraper

- **Professional Output**:
  - Downloads all media to organized `media/` folder
  - Generates `media_links.md` with comprehensive links
  - Includes statistics and metadata

- **Robust Error Handling**: Handles network issues, timeouts, and invalid URLs gracefully

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Quick Setup

```bash
# Clone or download the project
cd media-scraper

# Run the setup script (creates virtual environment and installs dependencies)
./setup.sh

# Or run directly
./run.sh
```

### Manual Installation

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the scraper
python media_scraper.py
```

## Usage

### Basic Usage

```bash
./run.sh
```

The script will prompt you for a URL:

```
=== Web Media Scraper ===
This tool scrapes all images and videos from a given URL
and saves them to a media folder with a markdown index.

Enter the URL to scrape (or 'quit' to exit): https://example.com
```

### Advanced Usage

```bash
# Activate virtual environment manually
source venv/bin/activate

# Run with specific URL
python media_scraper.py
```

## Output

After scraping, you'll get:

- **`media/` folder**: Contains all downloaded images and videos
- **`media_links.md`**: Markdown file with organized links and statistics

### Example Output Structure

```
media/
├── image1.png
├── image2.jpg
├── video1.mp4
└── ...

media_links.md
├── # Media Links from https://example.com
├── ## Images
│   ├── [image1.png](https://example.com/image1.png)
│   └── [image2.jpg](https://example.com/image2.jpg)
├── ## Videos
│   └── [video1.mp4](https://example.com/video1.mp4)
└── ## Statistics
    ├── Total Images: 2
    ├── Total Videos: 1
    └── Total Files: 3
```

## Configuration

### Customizing Filters

Edit the `exclude_patterns` set in `media_scraper.py` to customize which URLs are filtered out:

```python
self.exclude_patterns = {
    'facebook', 'twitter', 'instagram', 'linkedin', 'youtube', 'github',
    'logo', 'icon', 'favicon', 'avatar', 'profile', 'header', 'footer',
    # Add your custom patterns here
}
```

### Supported File Types

**Images**: .jpg, .jpeg, .png, .gif, .bmp, .webp, .svg, .ico, .tiff, .tif

**Videos**: .mp4, .avi, .mov, .wmv, .flv, .webm, .mkv, .m4v, .3gp, .ogv

## Dependencies

- `requests>=2.28.0` - HTTP requests
- `beautifulsoup4>=4.11.0` - HTML parsing
- `cloudscraper>=1.2.60` - Cloudflare bypass
- `lxml>=4.9.0` - XML/HTML parser

## Project Structure

```
media-scraper/
├── media_scraper.py      # Main scraper script
├── requirements.txt      # Python dependencies
├── setup.sh             # Automated setup script
├── run.sh               # Easy run script
├── README.md            # This file
├── LICENSE              # MIT License
├── .gitignore           # Git ignore rules
├── venv/                # Virtual environment (auto-created)
├── media/               # Downloaded media (auto-created)
└── media_links.md       # Generated markdown (auto-created)
```

## Troubleshooting

### Common Issues

1. **"externally-managed-environment" error**
   - Solution: Use the provided `setup.sh` script which creates a virtual environment

2. **ModuleNotFoundError: No module named 'requests'**
   - Solution: Run `./setup.sh` to install dependencies in virtual environment

3. **Cloudflare protection blocking access**
   - Solution: The script automatically uses cloudscraper to bypass protection

4. **No media found**
   - Check if the URL has accessible media files
   - Verify the URL is accessible in your browser

### Debug Mode

For debugging, you can modify the script to show more verbose output by editing the print statements in `media_scraper.py`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For issues and questions:
- Check the troubleshooting section above
- Verify your Python and pip installations
- Ensure the target URL is accessible

## Changelog

### v1.0.0
- Initial release
- Comprehensive media scraping
- Smart filtering system
- Cloudflare support
- Professional markdown output
- Virtual environment support

---

## About HackerX

HackerX is an open source organization focused on cybersecurity, offensive tooling, reconnaissance, and applied security research. Every repository published here is a direct reflection of hands-on work — built to solve real problems in the domain of cyber technology, ethical hacking, and security intelligence.

**Organization Philosophy**: Code that hacks. Research that matters. Everything shipped openly.

**Areas of Work**:
- **Offensive Tooling**: CLI tools and scripts for security testing
- **Reconnaissance & OSINT**: Information gathering and threat analysis
- **Security Auditing**: Professional-grade audit tooling
- **Scrapers & Automation**: Web scrapers and data extraction pipelines

**Founded & Led by**: Suryanshu Nabheet

---

**⚠️ Ethical Use Disclaimer**: This tool is intended for authorized security testing, educational purposes, and research only. Always respect website terms of service and robots.txt files when scraping content. Use responsibly and ethically.

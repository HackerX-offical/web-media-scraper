# Contributing to Web Media Scraper

Thank you for your interest in contributing to the Web Media Scraper project! This document provides guidelines for contributors.

## How to Contribute

### Reporting Issues

1. **Bug Reports**: If you find a bug, please create an issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (Python version, OS, etc.)

2. **Feature Requests**: For new features, please describe:
   - The feature you want
   - Why it would be useful
   - How you envision it working

### Development Setup

1. Fork the repository
2. Clone your fork locally
3. Set up the development environment:

```bash
# Clone your fork
git clone https://github.com/HackerX-offical/web-media-scraper.git
cd web-media-scraper

# Set up virtual environment
./setup.sh

# Activate environment
source venv/bin/activate
```

### Making Changes

1. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes following the coding standards below

3. Test your changes thoroughly

4. Commit your changes:
```bash
git add .
git commit -m "feat: add your feature description"
```

5. Push to your fork:
```bash
git push origin feature/your-feature-name
```

6. Create a Pull Request

## Coding Standards

### Python Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings for all functions and classes
- Keep functions focused and under 40 lines when possible
- Use type hints for function parameters and return values

### Example Code Style

```python
def extract_media_urls(self, html_content: str) -> Tuple[Set[str], Set[str]]:
    """
    Extract all image and video URLs from HTML content.
    
    Args:
        html_content: The HTML content to parse
        
    Returns:
        Tuple containing sets of image and video URLs
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    images = set()
    videos = set()
    
    # Implementation here
    return images, videos
```

### Commit Message Format

Use conventional commit format:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for code style changes
- `refactor:` for code refactoring
- `test:` for adding tests
- `chore:` for maintenance tasks

Examples:
```
feat: add support for additional video formats
fix: resolve Cloudflare bypass issue
docs: update installation instructions
```

## Testing

### Manual Testing

Before submitting a PR, please test:

1. **Basic functionality**: Run the scraper on several different websites
2. **Edge cases**: Test with URLs that have no media, only images, only videos, etc.
3. **Error handling**: Test with invalid URLs, network issues, etc.
4. **Filtering**: Verify that social media icons and UI elements are properly excluded

### Test Cases to Consider

- Websites with Cloudflare protection
- Sites with lazy-loaded images
- Pages with background images in CSS
- Sites with Open Graph meta tags
- YouTube/Vimeo embeds
- Various image and video formats
- Relative vs absolute URLs

## Pull Request Guidelines

### PR Requirements

1. **Clear Description**: Explain what your PR does and why
2. **Testing**: Mention how you tested your changes
3. **Documentation**: Update relevant documentation if needed
4. **No Breaking Changes**: Ensure existing functionality isn't broken

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Testing
How did you test these changes?

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated if needed
- [ ] No breaking changes introduced
```

## Project Structure Understanding

### Key Components

- **`media_scraper.py`**: Main scraper logic
  - `MediaScraper` class: Core functionality
  - `extract_media_urls()`: URL extraction from HTML
  - `should_exclude_url()`: Filtering logic
  - `download_file()`: File downloading

- **`setup.sh`**: Environment setup and dependency installation
- **`run.sh`**: Easy execution script
- **`requirements.txt`**: Python dependencies

### Adding New Features

When adding new features:

1. **Media Types**: To support new file formats, update the extension sets in `__init__()`
2. **Filtering**: To add new exclusion patterns, update `exclude_patterns` set
3. **Sources**: To add new media sources, update `extract_media_urls()` method
4. **Output**: To change output format, update `generate_markdown()` method

## Code Review Process

1. All PRs require review before merging
2. Maintainers will check for:
   - Code quality and style
   - Functionality and performance
   - Documentation completeness
   - Test coverage

## Getting Help

If you need help with contributing:

1. Check existing issues and PRs
2. Read the documentation thoroughly
3. Ask questions in issues (label as `question`)
4. Join discussions in existing PRs

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Web Media Scraper! Your contributions help make this project better for everyone.

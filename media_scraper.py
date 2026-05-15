#!/usr/bin/env python3
"""
Web Media Scraper
A comprehensive script to scrape images and videos from any URL
and generate a markdown file with all media links.
"""

import os
import re
import sys
import time
import requests
from urllib.parse import urljoin, urlparse
from pathlib import Path
from typing import List, Set, Tuple
from bs4 import BeautifulSoup
import cloudscraper

class MediaScraper:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.domain = urlparse(base_url).netloc
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.scraper = cloudscraper.create_scraper()
        
        # Find next available folder name (media, media-1, media-2, etc.)
        self.media_folder = self.get_next_available_folder()
        self.markdown_file = Path(f"{self.media_folder}_links.md")
        
        # Supported media extensions
        self.image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg', '.ico', '.tiff', '.tif'}
        self.video_extensions = {'.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mkv', '.m4v', '.3gp', '.ogv'}
        
        # Patterns to exclude (UI icons, social media, common web elements)
        self.exclude_patterns = {
            'facebook', 'twitter', 'instagram', 'linkedin', 'youtube', 'github', 'x.com', 'tiktok',
            'logo', 'icon', 'favicon', 'avatar', 'profile', 'header', 'footer', 'navbar', 'menu',
            'button', 'arrow', 'close', 'search', 'cart', 'share', 'like', 'comment', 'bookmark',
            'star', 'heart', 'bell', 'notification', 'settings', 'gear', 'user', 'login', 'signup',
            'download', 'upload', 'print', 'email', 'phone', 'location', 'calendar', 'clock',
            'chevron', 'caret', 'plus', 'minus', 'check', 'cross', 'x-mark', 'hamburger'
        }
        
    def get_next_available_folder(self) -> Path:
        """Find the next available folder name (media, media-1, media-2, etc.)"""
        counter = 0
        while True:
            if counter == 0:
                folder_name = "media"
            else:
                folder_name = f"media-{counter}"
            
            # Check if either the folder or the markdown file exists
            folder_path = Path(folder_name)
            markdown_path = Path(f"{folder_name}_links.md")
            
            if not folder_path.exists() and not markdown_path.exists():
                return folder_path
            counter += 1
    
    def create_media_folder(self):
        """Create media folder if it doesn't exist"""
        self.media_folder.mkdir(exist_ok=True)
        print(f"Created media folder: {self.media_folder}")
        
    def get_page_content(self, url: str) -> str:
        """Get page content, handling Cloudflare protection"""
        try:
            # First try with regular requests
            response = self.session.get(url, timeout=10)
            if response.status_code == 200:
                return response.text
        except Exception as e:
            print(f"Regular request failed: {e}")
            
        try:
            # Try with cloudscraper for Cloudflare protection
            response = self.scraper.get(url, timeout=15)
            if response.status_code == 200:
                return response.text
        except Exception as e:
            print(f"Cloudscraper request failed: {e}")
            
        return ""
        
    def extract_media_urls(self, html_content: str) -> Tuple[Set[str], Set[str]]:
        """Extract all image and video URLs from HTML content"""
        soup = BeautifulSoup(html_content, 'html.parser')
        images = set()
        videos = set()
        
        # Extract images from various sources
        for img in soup.find_all('img'):
            src = img.get('src') or img.get('data-src') or img.get('data-lazy-src')
            if src and not self.should_exclude_url(src):
                images.add(self.normalize_url(src))
                
        # Extract images from picture tags
        for picture in soup.find_all('picture'):
            for source in picture.find_all('source'):
                srcset = source.get('srcset') or source.get('data-srcset')
                if srcset:
                    for src in srcset.split(','):
                        src = src.strip().split()[0]  # Get URL part only
                        if src and not self.should_exclude_url(src):
                            images.add(self.normalize_url(src))
                        
        # Extract videos
        for video in soup.find_all('video'):
            src = video.get('src')
            if src and not self.should_exclude_url(src):
                videos.add(self.normalize_url(src))
            # Check source tags within video
            for source in video.find_all('source'):
                src = source.get('src')
                if src and not self.should_exclude_url(src):
                    videos.add(self.normalize_url(src))
                    
        # Extract videos from iframe (YouTube, Vimeo, etc.)
        for iframe in soup.find_all('iframe'):
            src = iframe.get('src')
            if src:
                if any(platform in src for platform in ['youtube.com', 'youtu.be', 'vimeo.com', 'dailymotion.com']):
                    videos.add(self.normalize_url(src))
                    
        # Extract background images from style attributes
        for element in soup.find_all(attrs={'style': True}):
            style = element.get('style', '')
            # Match url() patterns in CSS
            url_matches = re.findall(r'url\(["\']?(.*?)["\']?\)', style)
            for match in url_matches:
                if self.is_media_url(match) and not self.should_exclude_url(match):
                    images.add(self.normalize_url(match))
                    
        # Extract Open Graph meta tags
        for meta in soup.find_all('meta', attrs={'property': True}):
            property_name = meta.get('property', '').lower()
            if 'image' in property_name:
                content = meta.get('content')
                if content and not self.should_exclude_url(content):
                    images.add(self.normalize_url(content))
                    
        # Extract Twitter Card meta tags
        for meta in soup.find_all('meta', attrs={'name': True}):
            name = meta.get('name', '').lower()
            if 'image' in name:
                content = meta.get('content')
                if content and not self.should_exclude_url(content):
                    images.add(self.normalize_url(content))
                    
        return images, videos
        
    def normalize_url(self, url: str) -> str:
        """Convert relative URLs to absolute URLs"""
        if not url or url.startswith(('data:', 'blob:', 'javascript:')):
            return ""
            
        # Remove fragments and query parameters for cleaner URLs
        url = url.split('#')[0]
        
        # Convert relative to absolute
        if not url.startswith(('http://', 'https://')):
            url = urljoin(self.base_url, url)
            
        return url
        
    def is_media_url(self, url: str) -> bool:
        """Check if URL points to a media file"""
        if not url:
            return False
            
        parsed = urlparse(url)
        path = parsed.path.lower()
        
        # Check file extensions
        for ext in self.image_extensions | self.video_extensions:
            if path.endswith(ext):
                return True
                
        # Check common media patterns
        media_patterns = [
            r'/image/', r'/img/', r'/photo/', r'/picture/',
            r'/video/', r'/watch/', r'/stream/', r'/media/',
            r'cloudflare', r'cdn', r'assets'
        ]
        
        for pattern in media_patterns:
            if pattern in path.lower() or pattern in url.lower():
                return True
                
        return False
        
    def should_exclude_url(self, url: str) -> bool:
        """Check if URL should be excluded based on patterns"""
        if not url:
            return True
            
        url_lower = url.lower()
        filename = os.path.basename(urlparse(url).path).lower()
        
        # Check if filename or URL contains any exclude patterns
        for pattern in self.exclude_patterns:
            if pattern in url_lower or pattern in filename:
                return True
                
        # Check for very small images (likely icons/spacers)
        if any(size in filename for size in ['1x1', '2x2', 'spacer', 'pixel', 'dot']):
            return True
            
        return False
        
    def download_file(self, url: str, filename: str) -> bool:
        """Download a file from URL"""
        try:
            response = self.session.get(url, stream=True, timeout=30)
            response.raise_for_status()
            
            file_path = self.media_folder / filename
            
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        
            print(f"Downloaded: {filename}")
            return True
            
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            return False
            
    def get_filename_from_url(self, url: str, media_type: str) -> str:
        """Generate a unique filename from URL"""
        parsed = urlparse(url)
        original_name = os.path.basename(parsed.path)
        
        if original_name:
            # Clean filename
            original_name = re.sub(r'[^\w\-_.]', '', original_name)
            if not original_name:
                original_name = f"{media_type}_{hash(url) % 100000}"
        else:
            original_name = f"{media_type}_{hash(url) % 100000}"
            
        # Ensure unique filename
        counter = 1
        base_name = original_name
        while (self.media_folder / original_name).exists():
            name, ext = os.path.splitext(base_name)
            original_name = f"{name}_{counter}{ext}"
            counter += 1
            
        return original_name
        
    def scrape_media(self) -> Tuple[List[str], List[str]]:
        """Main scraping function"""
        print(f"Scraping media from: {self.base_url}")
        
        # Get page content
        html_content = self.get_page_content(self.base_url)
        if not html_content:
            print("Failed to fetch page content")
            return [], []
            
        # Extract media URLs
        images, videos = self.extract_media_urls(html_content)
        
        print(f"Found {len(images)} images and {len(videos)} videos")
        
        # Download files
        downloaded_images = []
        downloaded_videos = []
        
        for img_url in images:
            if img_url:
                filename = self.get_filename_from_url(img_url, "image")
                if self.download_file(img_url, filename):
                    downloaded_images.append((filename, img_url))
                    
        for video_url in videos:
            if video_url:
                filename = self.get_filename_from_url(video_url, "video")
                if self.download_file(video_url, filename):
                    downloaded_videos.append((filename, video_url))
                    
        return downloaded_images, downloaded_videos
        
    def generate_markdown(self, images: List[Tuple[str, str]], videos: List[Tuple[str, str]]):
        """Generate markdown file with media links"""
        content = f"# Media Links from {self.base_url}\n\n"
        content += f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        if images:
            content += "## Images\n\n"
            for filename, url in images:
                content += f"- [{filename}]({url})\n"
            content += "\n"
        else:
            content += "## Images\n\nNo images found.\n\n"
            
        if videos:
            content += "## Videos\n\n"
            for filename, url in videos:
                content += f"- [{filename}]({url})\n"
            content += "\n"
        else:
            content += "## Videos\n\nNo videos found.\n\n"
            
        # Add statistics
        content += "## Statistics\n\n"
        content += f"- Total Images: {len(images)}\n"
        content += f"- Total Videos: {len(videos)}\n"
        content += f"- Total Files: {len(images) + len(videos)}\n"
        
        # Write to file
        with open(self.markdown_file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Generated markdown file: {self.markdown_file}")
        
    def run(self):
        """Run the complete scraping process"""
        try:
            # Create media folder
            self.create_media_folder()
            
            # Scrape media
            images, videos = self.scrape_media()
            
            # Generate markdown
            self.generate_markdown(images, videos)
            
            print(f"\nScraping completed successfully!")
            print(f"Images downloaded: {len(images)}")
            print(f"Videos downloaded: {len(videos)}")
            print(f"Check the '{self.media_folder}' folder and '{self.markdown_file}'")
            
        except KeyboardInterrupt:
            print("\nScraping interrupted by user")
            sys.exit(1)
        except Exception as e:
            print(f"Error during scraping: {e}")
            sys.exit(1)

def main():
    """Main function to run the scraper"""
    print("=== Web Media Scraper ===")
    print("This tool scrapes all images and videos from a given URL")
    print("and saves them to a media folder with a markdown index.\n")
    
    while True:
        try:
            url = input("Enter the URL to scrape (or 'quit' to exit): ").strip()
            
            if url.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
                
            if not url:
                print("Please enter a valid URL")
                continue
                
            # Validate URL format
            if not (url.startswith('http://') or url.startswith('https://')):
                url = 'https://' + url
                
            # Create and run scraper
            scraper = MediaScraper(url)
            scraper.run()
            
            # Ask if user wants to continue
            another = input("\nScrape another URL? (y/n): ").strip().lower()
            if another not in ['y', 'yes']:
                break
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    main()

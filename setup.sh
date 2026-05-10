#!/bin/bash

echo "=== Media Scraper Setup ==="
echo "Setting up virtual environment and dependencies..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Setup completed successfully!"
    echo "To run the scraper:"
    echo "1. Activate the virtual environment: source venv/bin/activate"
    echo "2. Run the scraper: python media_scraper.py"
    echo ""
    echo "Or run directly with: ./run.sh"
else
    echo "❌ Setup failed. Please check the error messages above."
    exit 1
fi

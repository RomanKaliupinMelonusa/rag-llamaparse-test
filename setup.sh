#!/bin/bash

# Setup script for LlamaParse environment

echo "Setting up Python virtual environment for LlamaParse..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python version: $PYTHON_VERSION"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create virtual environment"
        exit 1
    fi
    echo "Virtual environment created successfully!"
else
    echo "Virtual environment already exists."
fi

# Upgrade pip
echo "Upgrading pip..."
venv/bin/pip install --upgrade pip --quiet

# Install dependencies
echo "Installing dependencies from requirements.txt..."
venv/bin/pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ Setup completed successfully!"
    echo ""
    echo "To activate the virtual environment, run:"
    echo "  source venv/bin/activate"
    echo ""
    echo "To use the LlamaParse script, run:"
    echo "  python llamaparse_ingest.py <file_path>"
    echo ""
    echo "Don't forget to set your API key in llamaparse_ingest.py!"
else
    echo "Error: Failed to install dependencies"
    exit 1
fi

#!/bin/bash

# Quick Setup Script for dubois-visualization-package
# This script helps you set up the repository on your local machine

echo "=========================================="
echo "dubois-visualization-package Repository Setup"
echo "=========================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install git first."
    exit 1
fi

echo "✓ Git is installed"

# Check if python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python 3 is installed"
python3 --version

echo ""
echo "Current directory: $(pwd)"
echo ""

# Ask if user wants to initialize git
read -p "Initialize git repository? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    if [ -d ".git" ]; then
        echo "⚠️  Git repository already initialized"
    else
        git init
        echo "✓ Git repository initialized"
    fi
fi

# Ask if user wants to create virtual environment
echo ""
read -p "Create Python virtual environment? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    if [ -d "venv" ]; then
        echo "⚠️  Virtual environment already exists"
    else
        python3 -m venv venv
        echo "✓ Virtual environment created"
        echo ""
        echo "To activate it, run:"
        echo "  source venv/bin/activate  # On Unix/Mac"
        echo "  venv\\Scripts\\activate     # On Windows"
    fi
fi

# Ask if user wants to install package
echo ""
read -p "Install package in development mode? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    if [ -d "venv" ]; then
        source venv/bin/activate
    fi
    pip install -e .
    echo "✓ Package installed in development mode"
fi

# Ask if user wants to run tests
echo ""
read -p "Run tests to verify installation? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    if command -v pytest &> /dev/null; then
        pytest tests/ -v
    else
        echo "⚠️  pytest not installed. Install with: pip install pytest"
    fi
fi

# Ask about GitHub connection
echo ""
echo "=========================================="
echo "GitHub Setup"
echo "=========================================="
echo ""
echo "To connect to GitHub:"
echo "1. Create a new repository on github.com named 'dubois-visualization-package'"
echo "2. Run these commands:"
echo ""
echo "   git add ."
echo "   git commit -m 'Initial commit: Phase 1 complete'"
echo "   git branch -M main"
echo "   git remote add origin https://github.com/YOUR_USERNAME/dubois-visualization-package.git"
echo "   git push -u origin main"
echo ""

read -p "Do you want to add git remote now? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    read -p "Enter your GitHub username: " username
    git remote add origin "https://github.com/$username/dubois-visualization-package.git"
    echo "✓ Remote added: https://github.com/$username/dubois-visualization-package.git"
    echo ""
    echo "Ready to push! Run:"
    echo "  git add ."
    echo "  git commit -m 'Initial commit'"
    echo "  git push -u origin main"
fi

echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Run examples: python examples/basic_usage.py"
echo "3. Read CONTRIBUTING.md for development guidelines"
echo "4. Check out PROJECT_SUMMARY.md for project overview"
echo ""
echo "Happy visualizing! 🎨"

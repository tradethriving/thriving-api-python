#!/bin/bash

# Setup script for publishing Thriving API Python SDK to GitHub and PyPI
# Run this from the SDK directory: ./setup_github.sh

set -e  # Exit on any error

echo "🚀 Setting up Thriving API Python SDK for GitHub and PyPI publishing..."

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: pyproject.toml not found. Please run this script from the SDK directory."
    exit 1
fi

# Check if GitHub CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI not found. Please install it first:"
    echo "   macOS: brew install gh"
    echo "   Or download from: https://cli.github.com/"
    exit 1
fi

# Check if user is authenticated with GitHub
if ! gh auth status &> /dev/null; then
    echo "🔐 Please authenticate with GitHub first:"
    gh auth login
fi

# Initialize git repository if not already done
if [ ! -d ".git" ]; then
    echo "📁 Initializing git repository..."
    git init
    git branch -M main
fi

# Add all files and commit
echo "📝 Adding files and creating initial commit..."
git add .
git commit -m "Initial release of Thriving API Python SDK v1.0.0" || echo "Files already committed"

# Create GitHub repository
echo "🏗️  Creating GitHub repository..."
if ! gh repo view tradethriving/thriving-api-python &> /dev/null; then
    gh repo create tradethriving/thriving-api-python \
        --public \
        --description "Official Python SDK for the Thriving API - AI-powered financial analysis and trading intelligence" \
        --homepage "https://tradethriving.com"
    
    # Add remote
    git remote add origin https://github.com/tradethriving/thriving-api-python.git || echo "Remote already exists"
else
    echo "Repository already exists"
fi

# Push to GitHub
echo "⬆️  Pushing to GitHub..."
git push -u origin main

# Install build dependencies
echo "🔧 Installing build dependencies..."
pip install build twine

# Build the package
echo "📦 Building package..."
python -m build

# Check the package
echo "✅ Checking package..."
twine check dist/*

echo ""
echo "🎉 Setup complete! Next steps:"
echo ""
echo "1. Set up PyPI accounts:"
echo "   - Production: https://pypi.org/account/register/"
echo "   - Test: https://test.pypi.org/account/register/"
echo ""
echo "2. Generate API tokens and add to GitHub secrets:"
echo "   - Go to: https://github.com/tradethriving/thriving-api-python/settings/secrets/actions"
echo "   - Add: PYPI_API_TOKEN and TEST_PYPI_API_TOKEN"
echo ""
echo "3. Create a release to trigger publishing:"
echo "   gh release create v1.0.0 --title 'v1.0.0 - Initial Release' --notes 'Initial release of the Thriving API Python SDK'"
echo ""
echo "4. Or test upload manually:"
echo "   twine upload --repository testpypi dist/*"
echo ""
echo "📁 Repository: https://github.com/tradethriving/thriving-api-python"
echo "📦 Built package files are in: ./dist/"

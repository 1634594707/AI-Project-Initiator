#!/bin/bash
# Setup script for AI Project Initiator

set -e

echo "🚀 Setting up AI Project Initiator..."

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✓ Found Python $PYTHON_VERSION"

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

# Check if Playwright is needed
read -p "Do you want to install Playwright for web testing? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🎭 Installing Playwright..."
    playwright install chromium
    echo "✓ Playwright installed"
fi

# Create .gitignore if it doesn't exist
if [ ! -f .gitignore ]; then
    echo "📝 Creating .gitignore..."
    cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
dist/
*.egg-info/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Project specific
docs/PRD.md
docs/MVP.md
docs/ROADMAP.md
docs/ARCHITECTURE.md
EOF
    echo "✓ .gitignore created"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Read the quick start guide: docs/guides/getting-started.md"
echo "2. Choose a preset: presets/README.md"
echo "3. Start your first project with: @project-init"
echo ""
echo "Happy building! 🎉"

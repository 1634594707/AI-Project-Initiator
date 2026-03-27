@echo off
REM Setup script for AI Project Initiator (Windows)

echo 🚀 Setting up AI Project Initiator...

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo ✓ Found Python %PYTHON_VERSION%

REM Install Python dependencies
echo 📦 Installing Python dependencies...
pip install -r requirements.txt

REM Ask about Playwright
set /p INSTALL_PLAYWRIGHT="Do you want to install Playwright for web testing? (y/n): "
if /i "%INSTALL_PLAYWRIGHT%"=="y" (
    echo 🎭 Installing Playwright...
    playwright install chromium
    echo ✓ Playwright installed
)

REM Create .gitignore if it doesn't exist
if not exist .gitignore (
    echo 📝 Creating .gitignore...
    (
        echo # Python
        echo __pycache__/
        echo *.py[cod]
        echo *$py.class
        echo *.so
        echo .Python
        echo env/
        echo venv/
        echo ENV/
        echo build/
        echo dist/
        echo *.egg-info/
        echo.
        echo # IDE
        echo .vscode/
        echo .idea/
        echo *.swp
        echo *.swo
        echo *~
        echo.
        echo # OS
        echo .DS_Store
        echo Thumbs.db
        echo.
        echo # Project specific
        echo docs/PRD.md
        echo docs/MVP.md
        echo docs/ROADMAP.md
        echo docs/ARCHITECTURE.md
    ) > .gitignore
    echo ✓ .gitignore created
)

echo.
echo ✅ Setup complete!
echo.
echo Next steps:
echo 1. Read the quick start guide: docs\guides\getting-started.md
echo 2. Choose a preset: presets\README.md
echo 3. Start your first project with: @project-init
echo.
echo Happy building! 🎉

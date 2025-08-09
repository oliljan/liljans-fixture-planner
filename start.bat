@echo off
echo 🚀 FPL Fixture Planner
echo =====================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python from https://python.org
    echo.
    pause
    exit /b 1
)

echo ✅ Python detected
echo.

REM Run the setup script
python setup.py

echo.
echo 🎉 If setup was successful, the planner should open in your browser!
echo 📁 If not, open fdr_fpl_team_picker.html manually
echo.
pause

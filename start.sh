#!/bin/bash

echo "🚀 FPL Fixture Planner"
echo "====================="
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    echo "Please install Python from https://python.org"
    echo
    exit 1
fi

echo "✅ Python 3 detected"
echo

# Make the script executable
chmod +x start.sh

# Run the setup script
python3 setup.py

echo
echo "🎉 If setup was successful, the planner should open in your browser!"
echo "📁 If not, open fdr_fpl_team_picker.html manually"
echo

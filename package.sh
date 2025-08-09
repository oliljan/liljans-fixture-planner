#!/bin/bash

echo "📦 Packaging FPL Fixture Planner..."
echo "=================================="

# Create package directory
PACKAGE_DIR="fpl-fixture-planner"
mkdir -p "$PACKAGE_DIR"

# Copy all necessary files
echo "📁 Copying files..."

# Core files
cp build_fdr.py "$PACKAGE_DIR/"
cp template.html "$PACKAGE_DIR/"
cp fdr_fpl_team_picker.html "$PACKAGE_DIR/"
cp requirements.txt "$PACKAGE_DIR/"
cp README.md "$PACKAGE_DIR/"

# Setup scripts
cp setup.py "$PACKAGE_DIR/"
cp start.bat "$PACKAGE_DIR/"
cp start.sh "$PACKAGE_DIR/"

# Quick start guide
cp START_HERE.txt "$PACKAGE_DIR/"

# Make shell script executable in the package
chmod +x "$PACKAGE_DIR/start.sh"

echo "✅ Files copied successfully!"

# Create zip file
echo "🗜️  Creating zip file..."
zip -r "fpl-fixture-planner.zip" "$PACKAGE_DIR/"

# Clean up
rm -rf "$PACKAGE_DIR"

echo "🎉 Package created: fpl-fixture-planner.zip"
echo ""
echo "📋 Package contents:"
echo "- build_fdr.py (main script)"
echo "- template.html (HTML template)"
echo "- fdr_fpl_team_picker.html (ready-to-use planner)"
echo "- requirements.txt (Python dependencies)"
echo "- setup.py (automated setup)"
echo "- start.bat (Windows launcher)"
echo "- start.sh (Mac/Linux launcher)"
echo "- README.md (detailed instructions)"
echo "- START_HERE.txt (quick start guide)"
echo ""
echo "📤 Ready to share with your friend!"
echo "💡 They just need to:"
echo "   1. Extract the zip file"
echo "   2. Run start.bat (Windows) or start.sh (Mac/Linux)"
echo "   3. Enjoy the planner!"

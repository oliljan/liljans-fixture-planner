#!/usr/bin/env python3
"""
FPL Fixture Planner Setup Script
Automatically installs dependencies and generates the HTML file.
"""

import subprocess
import sys
import os
import platform

def install_requirements():
    """Install required Python packages."""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages. Please check your Python installation.")
        return False

def generate_html():
    """Generate the HTML file from the template."""
    print("🔧 Generating HTML file...")
    try:
        subprocess.check_call([sys.executable, "build_fdr.py"])
        print("✅ HTML file generated successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to generate HTML file.")
        return False

def open_browser():
    """Open the HTML file in the default browser."""
    html_file = "fdr_fpl_team_picker.html"
    if os.path.exists(html_file):
        print("🌐 Opening in browser...")
        try:
            if platform.system() == "Darwin":  # macOS
                subprocess.run(["open", html_file])
            elif platform.system() == "Windows":
                subprocess.run(["start", html_file], shell=True)
            else:  # Linux
                subprocess.run(["xdg-open", html_file])
            print("✅ Browser opened!")
        except Exception as e:
            print(f"⚠️  Could not open browser automatically: {e}")
            print(f"📁 Please open {html_file} manually in your browser")
    else:
        print("❌ HTML file not found!")

def main():
    """Main setup function."""
    print("🚀 FPL Fixture Planner Setup")
    print("=" * 40)
    
    # Check if Python is available
    if sys.version_info < (3, 6):
        print("❌ Python 3.6 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    
    print(f"✅ Python {sys.version.split()[0]} detected")
    
    # Install requirements
    if not install_requirements():
        return False
    
    # Generate HTML
    if not generate_html():
        return False
    
    # Open browser
    open_browser()
    
    print("\n🎉 Setup complete!")
    print("📖 Check README.md for detailed usage instructions")
    print("🔄 To update fixture data later, run this script again")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        print("\n❌ Setup failed. Please check the error messages above.")
        input("Press Enter to exit...")
    else:
        input("\nPress Enter to exit...")

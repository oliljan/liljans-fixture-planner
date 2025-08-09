# FPL Fixture Planner

A comprehensive Fantasy Premier League fixture planning tool that helps you analyze player and team fixtures with difficulty ratings.

## 🚀 Quick Start

### Option 1: Simple Setup (Recommended)
1. **Download** the zip file
2. **Extract** all files to a folder
3. **Run** `generate.bat` (Windows) or `generate.sh` (Mac/Linux)
4. **Open** `fdr_fpl_team_picker.html` in your browser

### Option 2: Manual Setup
1. **Install Python** (if not already installed)
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Generate HTML**: `python build_fdr.py`
4. **Open** `fdr_fpl_team_picker.html` in your browser

## 📁 File Structure
```
fpl-fixture-planner/
├── build_fdr.py              # Main script to generate HTML
├── template.html             # HTML template
├── fdr_fpl_team_picker.html # Generated webpage (open this!)
├── requirements.txt          # Python dependencies
├── generate.bat             # Windows setup script
├── generate.sh              # Mac/Linux setup script
└── README.md               # This file
```

## 🎯 Features

### Player Planning
- **15-player squad** management
- **Drag & drop** player reordering
- **Position-based color coding** (GK, DEF, MID, FWD)
- **Player cost display** in dropdowns
- **Squad total cost** calculation
- **Add/remove rows** dynamically

### Template Management
- **Save templates** with custom names
- **Load saved templates** from dropdown
- **Delete templates** as needed
- **Persistent storage** in browser

### Team Integration
- **Fetch real FPL team** by entering your team ID
- **Persistent team state** - remembers your planning when you fetch the same team again
- **Automatic player loading** from your actual squad

### Fixture Analysis
- **FDR color coding** (green=easy, red=hard)
- **Interactive fixtures** - click to hide/show
- **GW highlighting** - click headers to highlight columns
- **Player count tracking** - shows X/11 players per gameweek
- **Visual feedback** for complete teams (11/11)

### Team Fixture Table
- **All 20 teams** displayed
- **Synchronized scrolling** with player table
- **Same FDR coding** for consistency
- **Complete fixture view** for all teams

### Quick Filters
- **Position filters** (GK, DEF, MID, FWD)
- **Team filters** (all Premier League teams)
- **Combined filtering** (e.g., "Arsenal defenders")
- **Dropdown filtering** - only affects dropdown options, not table

## 🎮 How to Use

### Basic Setup
1. Open `fdr_fpl_team_picker.html` in your browser
2. The planner loads with empty player slots
3. Start by either:
   - **Fetching your team**: Enter your FPL team ID and click "Fetch Real Team"
   - **Loading a template**: Use the "Load Saved Templates" dropdown
   - **Manual setup**: Select players from the dropdowns

### Player Management
- **Select players** from the dropdowns in the Squad column
- **Drag & drop** players to reorder rows
- **Add rows** with the "Add Player Row" button
- **Remove rows** with the "Remove Last Row" button

### Template Management
- **Save template**: Enter a name and click "Save Template"
- **Load template**: Select from dropdown and click "Load Template"
- **Delete template**: Select and click "Delete Template"

### Fixture Planning
- **Hide fixtures**: Click any fixture to hide it (click again to show)
- **GW highlighting**: Click gameweek headers to highlight that column
- **View team fixtures**: Scroll down to see the team fixture table
- **Synchronized scrolling**: Both tables scroll together horizontally

### Quick Filters
- **Position filters**: Click GK, DEF, MID, FWD to filter dropdowns
- **Team filters**: Click team abbreviations to filter by team
- **Combined filters**: Use both position and team filters together
- **Clear filters**: Click "ALL" to reset filters

## 🔧 Technical Details

### Requirements
- **Python 3.6+** (for data generation)
- **Modern web browser** (Chrome, Firefox, Safari, Edge)
- **Internet connection** (for fetching FPL data)

### Data Sources
- **FPL API**: Real-time player and fixture data
- **Local storage**: Templates and team states saved in browser
- **Auto-refresh**: Data updates when you run the generation script

### Browser Compatibility
- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ❌ Internet Explorer (not supported)

## 🛠️ Troubleshooting

### Common Issues

**"Python not found"**
- Install Python from python.org
- Make sure Python is in your system PATH

**"Module not found"**
- Run: `pip install -r requirements.txt`

**"Can't open HTML file"**
- Right-click the HTML file → "Open with" → Choose your browser
- Or drag the HTML file into your browser window

**"FPL team not loading"**
- Check your team ID is correct
- Ensure you have internet connection
- Try refreshing the page

**"Templates not saving"**
- Check browser permissions for local storage
- Try a different browser
- Clear browser cache and try again

### Getting Your FPL Team ID
1. Log into fantasy.premierleague.com
2. Go to your team page
3. Look at the URL: `https://fantasy.premierleague.com/entry/YOUR_ID/event/1`
4. The number after `/entry/` is your team ID

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Try refreshing the page
3. Clear browser cache and try again
4. Ensure you have the latest version of the files

## 🔄 Updates

To get the latest fixture data:
1. Run `generate.bat` (Windows) or `generate.sh` (Mac/Linux)
2. Refresh your browser
3. The planner will now have updated fixture information

---

**Enjoy planning your FPL strategy!** 🏆

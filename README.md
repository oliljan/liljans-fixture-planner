# Liljan's Fixture Planner

A comprehensive Fantasy Premier League fixture planning tool with interactive features, drag-and-drop functionality, and position-based color coding.

## Features

- **Interactive Fixture Planning**: Click fixtures to hide/show gameweeks based on player position
- **Drag & Drop**: Reorder players by dragging rows
- **Position Color Coding**: 
  - Goalkeepers: Teal (#20B2AA)
  - Defenders: Orange (#FF8C00)
  - Midfielders: Light Beige (#F5F5DC)
  - Forwards: Dark Blue (#1E3A8A)
- **Template Management**: Save, load, and delete team templates
- **FPL Integration**: Fetch real FPL teams by team ID
- **Dynamic Rows**: Add/remove player rows as needed
- **Starting 11 vs Bench**: Visual separator between starting 11 and bench players

## Quick Start

### Option 1: Direct HTML File (Recommended)
1. Download `fdr_fpl_team_picker.html`
2. Double-click to open in any web browser
3. Start planning your FPL team!

### Option 2: Generate Fresh Data
1. Ensure Python 3.6+ is installed
2. Install required packages: `pip install requests jinja2`
3. Run: `python3 build_fdr.py`
4. Open the generated `fdr_fpl_team_picker.html` file

## How to Use

### Basic Usage
1. **Select Players**: Choose players from the dropdown menus
2. **Drag & Drop**: Reorder players by dragging rows
3. **Interactive Fixtures**: Click any fixture to hide/show gameweeks
4. **Save Templates**: Enter a name and click "Save Template"
5. **Load Templates**: Select from dropdown and it loads automatically

### Advanced Features
- **Fetch Real Team**: Enter your FPL team ID to load your actual team
- **Add/Remove Rows**: Use buttons below the table to adjust squad size
- **Fixture Focus**: 
  - Starting 11: Click fixture → hides future gameweeks
  - Bench: Click fixture → hides past gameweeks
  - Click again to restore all fixtures

## File Structure

```
fixturePlanner/
├── build_fdr.py          # Python script to fetch FPL data and generate HTML
├── template.html         # HTML template with all styling and functionality
├── fdr_fpl_team_picker.html  # Generated HTML file (ready to use)
└── README.md            # This file
```

## Requirements

- **For Generation**: Python 3.6+, requests, jinja2
- **For Usage**: Any modern web browser (Chrome, Firefox, Safari, Edge)

## Data Sources

- FPL API: https://fantasy.premierleague.com/api/
- Automatically fetches latest player data and fixtures
- Updates when you run `build_fdr.py`

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Any modern browser with JavaScript enabled

## Troubleshooting

### If the HTML file doesn't work:
1. Check that JavaScript is enabled in your browser
2. Try opening in Chrome or Firefox
3. Ensure the file is complete (should be ~50KB)

### If you want fresh data:
1. Run `python3 build_fdr.py`
2. Use the newly generated HTML file

## Features in Detail

### Position Color Coding
- **Goalkeepers**: Teal background
- **Defenders**: Orange background  
- **Midfielders**: Light beige background
- **Forwards**: Dark blue background

### Interactive Fixtures
- Click any fixture to focus on specific gameweeks
- Starting 11 players: hides future gameweeks
- Bench players: hides past gameweeks
- Click again to restore all fixtures

### Template System
- Save unlimited team templates
- Auto-load when selecting from dropdown
- Update existing templates by saving with same name

### Drag & Drop
- Drag any player row to reorder
- Maintains all fixture states during reordering
- Smooth animations and visual feedback

## Support

For issues or questions, check that:
1. All files are in the same folder
2. You're using a modern web browser
3. JavaScript is enabled
4. The HTML file is complete and not corrupted

The tool is completely self-contained once generated - no internet connection required for usage!


import requests
import json
from jinja2 import Template

NUM_ROWS = 15
DEFAULT_GW_RANGE = 6

# Fetch FPL data
bootstrap = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/").json()
fixtures = requests.get("https://fantasy.premierleague.com/api/fixtures/").json()

# Prepare teams and players
teams = {team["id"]: team["name"] for team in bootstrap["teams"]}
team_shorts = {team["id"]: team.get("short_name", team["name"]) for team in bootstrap["teams"]}
players = [{
    "id": p["id"],
    "web_name": p["web_name"],
    "team_id": p["team"],
    "team_name": teams[p["team"]],
    "team_short": team_shorts[p["team"]],
    "position": p["element_type"],
    "now_cost": p["now_cost"]
} for p in bootstrap["elements"]]

# Prepare fixtures per team
team_fixtures = {}
for fixture in fixtures:
    if not fixture["event"]:
        continue
    for is_home in [True, False]:
        team_id = fixture["team_h"] if is_home else fixture["team_a"]
        opp_team = fixture["team_a"] if is_home else fixture["team_h"]
        difficulty = fixture["team_h_difficulty"] if is_home else fixture["team_a_difficulty"]
        loc = "H" if is_home else "A"
        entry = {
            "event": fixture["event"],
            "opponent": teams[opp_team],
            "difficulty": difficulty,
            "location": loc
        }
        team_fixtures.setdefault(team_id, []).append(entry)

# Load HTML template from file
with open("template.html", "r", encoding="utf-8") as f:
    template = Template(f.read())

# Render HTML
html_output = template.render(
    num_rows=NUM_ROWS,
    default_gws=DEFAULT_GW_RANGE,
    players_json=json.dumps(players),
    fixtures_json=json.dumps(team_fixtures),
    teams=teams,
    team_shorts=team_shorts
)

# Save output HTML
with open("fdr_fpl_team_picker.html", "w", encoding="utf-8") as f:
    f.write(html_output)

print("✅ HTML created: fdr_fpl_team_picker.html")

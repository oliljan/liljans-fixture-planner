// Template Restore Script
// Run this in the browser console to restore sample templates

function restoreSampleTemplates() {
  // Sample template 1: Balanced team
  const balancedTeam = {
    players: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    hiddenFixtures: []
  };
  
  // Sample template 2: Attack-focused team
  const attackTeam = {
    players: [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    hiddenFixtures: ["0-1", "1-2", "2-3"]
  };
  
  // Sample template 3: Defensive team
  const defensiveTeam = {
    players: [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45],
    hiddenFixtures: ["5-10", "6-11", "7-12"]
  };
  
  // Save templates to localStorage
  localStorage.setItem("fpl_team_Balanced_Team", JSON.stringify(balancedTeam));
  localStorage.setItem("fpl_team_Attack_Focused", JSON.stringify(attackTeam));
  localStorage.setItem("fpl_team_Defensive_Setup", JSON.stringify(defensiveTeam));
  
  console.log("Sample templates restored!");
  console.log("Templates created:");
  console.log("- Balanced_Team");
  console.log("- Attack_Focused");
  console.log("- Defensive_Setup");
  
  // Refresh the page to see the templates
  location.reload();
}

// Instructions
console.log("To restore sample templates, run: restoreSampleTemplates()");

import json

def save_match_data(match):

    match_data = {
        "team1": match.team1.name,
        "team2": match.team2.name,
        "score1": match.team1.total_runs,
        "score2": match.team2.total_runs,
        "winner": match.winner,

        "players_team1": [
            {
                "name": player.name,
                "runs": player.runs,
                "wickets": player.wickets
            }
            for player in match.team1.players
        ],

        "players_team2": [
            {
                "name": player.name,
                "runs": player.runs,
                "wickets": player.wickets
            }
            for player in match.team2.players
        ]
    }

    try:
        with open("data/matches.json", "r") as file:
            matches = json.load(file)
    except:
        matches = []

    matches.append(match_data)
    with open("data/matches.json", "w") as file:
        json.dump(matches, file, indent=4)

def load_match_data():
    try:
        with open("data/matches.json", "r") as file:
            return json.load(file)
    except:
        return []

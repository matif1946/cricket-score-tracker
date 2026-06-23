from models import Match, Team, Player

def show_menu():
    print("/n ===== Cricket Score Tracker =====")
    print("1. Create Match")
    print("2. Previous Matches")
    print("3. Exit")

def create_match():
    team1_name = input("Enter Team 1 Name: ")
    team2_name = input("Enter Team 2 Name: ")

    team1 = Team(team1_name)
    team2 = Team(team2_name)

    num_players = int(input("Enter number of players in each team: "))

    for i in range(num_players):
        player_name = input(f"Enter name of player {i+1} for {team1_name}: ")
        team1.add_player(Player(player_name))

    for i in range(num_players):
        player_name = input(f"Enter name of player {i+1} for {team2_name}: ")
        team2.add_player(Player(player_name))

    team1.total_runs = int(input(f"Enter total runs scored by {team1_name}: "))
    team2.total_runs = int(input(f"Enter total runs scored by {team2_name}: "))

    match = Match(team1, team2)
    match.calculate_winner()
    print(f"The winner is: {match.winner}")


class Player:
    def __init__(self, name):
        self.name = name
        self.runs = 0
        self.wickets = 0

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.total_runs = 0
        self.total_wickets = 0

    def add_player(self, player):
        self.players.append(player)

    def update_stats(self, player_name, runs=0, wickets=0):
        for player in self.players:
            if player.name == player_name:
                player.runs += runs
                player.wickets += wickets
                break

class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        
        winner = None
    def calculate_winner(self):
        if self.team1.total_runs > self.team2.total_runs:
            self.winner = self.team1.name
        elif self.team2.total_runs > self.team1.total_runs:
            self.winner = self.team2.name
        else:
            self.winner = "Its a draw"

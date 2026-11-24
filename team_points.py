scores = {}
teams = {}

def points_by_team(scores, teams):
    pointsByTeam = {}
    for team, players in teams.items():
        teamPoints = 0
        for player in players:
            teamPoints += scores[player]
        pointsByTeam[team] = teamPoints
    return pointsByTeam

try:
    with open('players.txt') as file:
        for line in file:
            line = line.strip()
            if line:
                name, points, team = line.split()
                scores[name] = int(points)

                if team in teams:
                    teams[team].append(name)
                else:
                    teams[team] = [name]
except FileNotFoundError:
    print('an error occured while opening the file')

print('Scores: ', scores)
print('Teams: ', teams)
print('Points by team: ', points_by_team(scores, teams))

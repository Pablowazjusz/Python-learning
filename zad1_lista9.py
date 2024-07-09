import random

teams = ["Real Madrid", "Barcelona", "Manchester United", "Paris Saint-Germain", "Bayern Munich", "Liverpool", "Chelsea", "Juventus", "Arsenal", "Manchester City", "Tottenham", "Atletico Madrid", "Borussia Dortmund", "Inter Milan", "AC Milan", "Roma", "Napoli", "Lazio", "Fiorentina", "Sevilla"]

team_sets = []

for i in range(4):
    set_teams = random.sample(teams, 10)
    team_sets.append(set(set_teams))

print(team_sets)

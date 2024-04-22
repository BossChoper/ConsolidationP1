sided_die = []
sided_die_rolls = {}
sides = int(input("Enter a number: "))

for side in range(1, sides + 1):
    sided_die.append(side)
    new_pair = {side : 0}
    sided_die_rolls.update(new_pair)
print(sided_die)
print(sided_die_rolls)

players = []
players_dict = {}
playerCount = int(input("Give an integer: "))
for player in range(1, playerCount):
    number = player
    key = f"Player {player}"
    players.append(player)
    players_dict[key] = 0
    #use an f string (print(f" ")) to input players
    print(f"Player {player}")
print(players)
print(players_dict)

def changePlayerCount():
    playerCount = int(input("Give an integer for player count: "))
    for player in range(1, playerCount):
        key = f"Player {player}"
        players.append(player)
        players_dict[key] = 0
    print(players)
    print(players_dict)
    #use an f string (print(f" ")) to input players
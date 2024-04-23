import random
sided_die = []
sided_die_rolls = {}
sides = int(input("Enter a number: "))

for side in range(1, sides + 1):
    sided_die.append(side)
    new_pair = {side : 0}
    sided_die_rolls.update(new_pair)
print(sided_die)
print(sided_die_rolls)

players = [1, 2]
players_dict = {1 : 0, 2 : 0}
sidesRolled = []
sidesRolledDict = {}

print(players_dict)
def printAllPlayerInfo():
    playerCount = 2
    for player in range(1, playerCount + 1):
        #side1Points, side2Points, side3Points = points
        #need to take key and associated item and print them out for each player
        #print(f"{player} got {side1Points} for one side, {side2Points} for second side, {side3Points} for third side")
        #print(player)
        printPlayer = players_dict[player]
        print(f"{printPlayer} is the appropriate score for Player: {player}")

printAllPlayerInfo()
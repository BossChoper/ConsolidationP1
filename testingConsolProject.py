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

players = []
players_dict = {}
sidesRolled = []
sidesRolledDict = {}

    #initial roll. Rolls all dies and stores in results list/dictionary
for index in range(3):
    current_roll = random.choice(sided_die)
    #below adds temporary roll results to the list
    sidesRolled.append(current_roll)
    #below records the numbers rolled and their frequency

print(sidesRolled)
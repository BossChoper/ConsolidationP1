sided_die = []
sided_die_rolls = {}
sides = int(input("Enter a number: "))

for side in range(1, sides + 1):
    sided_die.append(side)
    new_pair = {side : 0}
    sided_die_rolls.update(new_pair)
print(sided_die)
print(sided_die_rolls)
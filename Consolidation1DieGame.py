import random
#Testing document

practice_results = []
practice_dictionary = {1: 0, 2 : 0}
all_practice_results = {1 : 0}
two_sided_die = (1, 2)

#turn 1 for player 1
turn = 0
players = [1]

#initial roll. Rolls all dies and stores in results list/dictionary
for index in range(3):
    current_roll = random.choice(two_sided_die)
    practice_results.append(current_roll)
    practice_dictionary[current_roll] += 1

#initial roll results
print(practice_dictionary)
print(practice_results)

#checking if two rolls are the same
if practice_results[0] == practice_results[1] or practice_results[1] == practice_results[2] or practice_results[0] == practice_results[2]:
        print("Two rolls are the same")

#variable for the odd die
odd_die = 0

#if two rolls are the same, reroll the odd roll
def whichRollDifferent():
    if practice_results[0] != practice_results[1] and practice_results[0] != practice_results[2]:
        odd_die = 1 #the first number is the odd one out
    elif practice_results[1] != practice_results[0] and practice_results[1] != practice_results[2]:
        odd_die = 2 #the second number is the odd one out
    else:
        odd_die = 3 #the third number is the odd one out

#rerolling a die based on which die was found to be different
def rerollOddDie():
    if odd_die == 1:
        practice_results[0] = random.randint(1,2)
    elif odd_die == 2:
        practice_results[1] = random.randint(1,2)
    else:
        practice_results[2] = random.randint(1,2)


#checking if all rolls are the same
def isTupledOut():
    if practice_results[0] == practice_results[1] and practice_results[0] == practice_results[2]:
            print("All rolls are the same. Tupled out!")
            #take away points, no points will be added

#confirmation of final results
print(practice_dictionary)
print(practice_results)


#add up total points for turn scoring
total_points = 0

#adds all numbers together in current roll results
def addUpPoints():
    for int in practice_results:
        total_points += int
    print(total_points)

#goal to reach to win game for one player
limit_score = 50

#checks if any players rearched 50 points or game is over five turns
#needs to be finished
def isGameOver():
    if total_points == limit_score:
         print("Game Over")

#shows current score for all players when called
#needs to be finished
def displayScore():
     print(practice_results)

#keeps track of who has highest score
#needs to be finished
def highScore():
     if total_points > 1:
          print(total_points)

#changes number of sides to roll
#needs to be finished
def changeDieSides():
     two_sided_die

#testing player dictionary
player_data = {"Player 1": (0, 1, 2),
               "Player 2": (0, 1, 2)}
player_data["Player 1"]
player_data.keys()

#print each player in the list one by one
def printAllPlayers():
    for player in player_data.keys():
     print(player)

#print out each player and their associated items
def printAllPlayerInfo():
    for player, points in player_data.items():
     side1Points, side2Points, side3Points = points
     print(f"{player} got {side1Points} for one side, {side2Points} for second side, {side3Points} for third side")
     print(player)
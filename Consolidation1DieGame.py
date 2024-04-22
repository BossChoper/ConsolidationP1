import random
#Testing document
#In this practice, one player rolls between two numbers

#GLOBAL VARIABLE LIST-----------------------

#list to store all rolled numbers.
practice_results = []
#dictionary to store results and organize into categories, preferably per player
practice_dictionary = {1: 0, 2 : 0}
#save all results total
all_practice_results = {1 : 0}

#die for testing is two sided
two_sided_die = (1, 2)
#this is the die the player will set
sided_die = []
#below is to be updated with sided_die in accordance
sided_die_rolls = {}

#turn 1 for player 1
turn = 0
players = []
#append players to the list

#goal to reach to win game for one player
limit_score = 50

#add up total points for turn scoring
total_points = 0

#variable for the odd roll side when comparing
odd_die = 0

#variables keep track of player data
player = []
player_data = {}

#METHOD LIST ----------------------------------
def completeRoll(sided_die):
    side_results
    #completes a set of rolls for one player
    for index in range(sided_die):
        current_roll = random.choice(sided_die)
        practice_results.append(current_roll)
        practice_dictionary[current_roll] += 1

#initial roll. Rolls all dies and stores in results list/dictionary
def practiceDieRoll():
    #range(3) will roll a die three times and store in the results
    for index in range(3):
        #randomly picks one number from two sided die, between 1 and 2
        current_roll = random.choice(two_sided_die)
        practice_results.append(current_roll)
        #below adds it to the appropriate section in dictionary
        practice_dictionary[current_roll] += 1
    #initial roll results
    print(practice_dictionary)
    print(practice_results)

#checking if two rolls are the same in three
#finished (could be expanded)
def checkForTwoRolls():
    if practice_results[0] == practice_results[1] or practice_results[1] == practice_results[2] or practice_results[0] == practice_results[2]:
        print("Two rolls are the same")

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
#finished (could be expanded)
def isTupledOut():
    if practice_results[0] == practice_results[1] and practice_results[0] == practice_results[2]:
            print("All rolls are the same. Tupled out!")
            #take away points, no points will be added

#confirmation of final results
print(practice_dictionary)
print(practice_results)


#adds all numbers together in current roll results
#needs to be finished
def addUpPoints():
    for int in practice_results:
        total_points += int
    print(total_points)

#checks if any players rearched 50 points or game is over five turns
#needs to be finished
def isGameOver():
    if total_points == limit_score:
         print("Game Over")

#ends game at the fifth turn
#finished
def endFiveTurns():
    #ends game if this is the end of the fifth turn
    if turn == 6:
        print("Alright, game is over.")

#shows current score for all players when called
#needs to be tested
def displayScore():
    checkDisplayInterest = int(input("Do you want to see all player scores? Enter 1 for yes, 2 for no: "))
    if checkDisplayInterest == 1:
         printAllPlayerInfo()
    else:
        print("Okay, keep playing. ")
    print(practice_results)

#keeps track of who has highest score
#needs to be finished
def highScore():
     if total_points > 1:
          print(total_points)

#changes number of sides to roll
#finished
def changeDieSides(sides):
    #sides = int(input("Enter a number: "))
    for side in range(1, sides + 1):
        sided_die.append(side)
        add_side = {side: 0}
        #adds side to the roll dictionary
        sided_die_rolls.update(add_side)
    #both variables should have the same sides
    print(sided_die)
    print(sided_die_rolls)

#print each player's name in the list one by one
#finished
def printAllPlayers():
    for player in player_data.keys():
        print(player)

#print out each player and their associated items
#needs to be tested
def printAllPlayerInfo():
    for player, points in player_data.items():
        side1Points, side2Points, side3Points = points
        print(f"{player} got {side1Points} for one side, {side2Points} for second side, {side3Points} for third side")
        print(player)
    
#testing: player dictionary
def testData():
    player_data = {"Player 1": (0, 1, 2),
                   "Player 2": (0, 1, 2)}
    player_data["Player 1"]
    player_data.keys()

#Testing: a full program for the game
print("Hello, welcome to TupledOut.")
dieCount = int(input("Give an integer for the die sides: "))
changeDieSides(dieCount)

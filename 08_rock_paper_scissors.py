#! python3

import random

choiceLookup = {'rock':0, 'scissors':1, 'paper':2}

def checkBattle(choice1, choice2):
    if choice1 == choice2:
        return False
    elif (choiceLookup[choice1] + 2) % 3 == choiceLookup[choice2]:
        return choice2
    else:
        return choice1

def userInputToChoice(letter):
    if letter == 'r' or letter == 'R':
        return 'rock'
    elif letter == 's' or letter == 'S':
        return 'scissors'
    elif letter == 'p' or letter == 'P':
        return 'paper'
    else:
        return False

def getUserChoice():
    choice = input("Choose: (r)ock, (s)cissors or (p)aper: ")
    return userInputToChoice(choice)

def getRandomChoice():
    return random.choice(list(choiceLookup.keys()))

while True:
    userChoice = getUserChoice()
    if userChoice == False:
        print('It is not a valid choice. Type again!')
        continue

    enemyChoice = getRandomChoice()
    print('You: ' + userChoice + ", enemy: " + str(enemyChoice))
    winner = checkBattle(userChoice, enemyChoice)
    if winner == userChoice:
        print("You won!")
    elif winner == enemyChoice:
        print("Computer won!")
    else:
        print("Draw!")


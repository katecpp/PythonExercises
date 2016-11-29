#! python3
import random

def getFeedback():
    value = ""
    possibleAnswers = ["l", "g", "e"]
    while value not in possibleAnswers:
        value = input("Press l for lower, g for greater, e for equal: ")
        if len(value) > 1:
            value = value[0]
        if value not in possibleAnswers:
            print("I don't understand!")
    return value

min = 1
max = 100
middleValue = 0
iteration = 0
print("Think about the number from range {0} - {1}.".format(min, max))
input("Are you ready? Press enter!\n")

while True:
    iteration = iteration + 1
    oldMiddleValue = middleValue
    middleValue = (min + max)//2
    if oldMiddleValue == middleValue:
        print("You cheater!")
        break
    print("Is it {0}?".format(middleValue))
    feedback = getFeedback()
    if feedback == "l":
        max = middleValue - 1
    elif feedback == "g":
        min = middleValue + 1
    else:
        print("I guessed with only {0} tries!".format(iteration))
        break



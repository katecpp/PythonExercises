#! python3
import random

def readIntegerAsString(length):
    value = ""
    accepted = False
    while accepted == False:
        value = input(">>>> ")
        if value.isdigit() == False:
            print("This is not a number!")
        elif len(value) != length or len(set(value)) != length:
            print("Number should contain " + str(length) + " unique digits.")
        else:
            accepted = True
    return str(value)

def getRandomNumber(length):
    digits = list("0123456789")
    length = min(len(digits), length)
    random.shuffle(digits)
    return digits[0:length]

def processGuess(secretNumber, guessedNumber):
    cowsBulls = [0, 0]
    for i in range(0, len(secretNumber)):
        if secretNumber[i] == guessedNumber[i]:
            cowsBulls[0] += 1
        elif guessedNumber[i] in secretNumber:
            cowsBulls[1] += 1
    return cowsBulls

if __name__=="__main__":
    print("Welcome to the Cows and Bulls Game!")
    numberLength = 4
    secretNumber = getRandomNumber(numberLength)
    while True:
        print("Enter a " + str(numberLength) + " digit number:")
        guess = readIntegerAsString(numberLength)
        cowsAndBulls = processGuess(secretNumber, guess)
        if cowsAndBulls[0] == numberLength:
            print("You won!")
            break
        else:
            print(str(cowsAndBulls[0]) + " cows, " + str(cowsAndBulls[1]) + " bulls.")

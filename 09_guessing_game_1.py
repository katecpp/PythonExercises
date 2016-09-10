#! python3
import random

def readInteger():
    value = ""
    while value.isdigit() == False:
        value = input("Enter your guess: ")
        if value.isdigit() == False:
            print("This is not a number!")
    return int(value)

print("Choosing a secret value...")
secretValue = random.randint(1, 9)
failuresNumber = 0

while True:
    guess = readInteger()
    if guess == secretValue:
        print("You won with " + str(failuresNumber) + " failures.")
        break
    else:
        failuresNumber = failuresNumber + 1
        if guess < secretValue:
            print("More!")
        else:
            print("Less!")


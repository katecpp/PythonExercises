#! python3
import random

lowerLetters = "abcdefghijklmnoprstuwyz"
upperLetters = lowerLetters.upper()
specialSigns = "!@#$%^&*()-:.?"
numbers = "1234567890"

def readInteger():
    value = ""
    while value.isdigit() == False:
        value = input("Your choice: ")
        if value.isdigit() == False:
            print("This is not a number!")
    return int(value)

def generatePassword(strongLvl):
    password = [random.choice(lowerLetters) for _ in range(1,7)]
    if (strongLvl > 1):
        password += "".join([random.choice(upperLetters) for _ in range(1,4)])
        password += "".join([random.choice(numbers) for _ in range(1,3)])
    if (strongLvl > 2):
        password += "".join([random.choice(specialSigns) for _ in range(1,3)])
    random.shuffle(password)
    return "".join(password)

print("__Password generator__\n");
print("Choose mode:\n");
print("1 - weak password\n");
print("2 - medium password\n");
print("3 - strong password\n");
strongLevel = readInteger()
pwd = generatePassword(strongLevel)
print("Password: " + pwd)


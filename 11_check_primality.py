#! python3

import math

def readInteger():
    value = ""
    while value.isdigit() == False:
        value = input("Check primality of number: ")
        if value.isdigit() == False:
            print("This is not a number!")
    return int(value)

def isPrime(number):
    upperBound = int(math.sqrt(number))
    for d in range(2, upperBound+1):
        if number % d == 0:
            return False
    return True

value = readInteger()
print(str(value) + (" is " if isPrime(value) else " is not ") + "prime")


#! python3
import random

def generateRandom(valueMin, valueMax):
    return valueMin + (int)(random.random() * valueMax)

def generateRandomArr(maxLength, valueMin, valueMax):
    length = generateRandom(1, maxLength)
    return [generateRandom(valueMin, valueMax) for _ in range(length)]

a = generateRandomArr(20, 0, 50)
b = generateRandomArr(20, 0, 50)

print(a)
print(b)

aSet = set(a)
bSet = set(b)

common = aSet.intersection(bSet)
print(common)

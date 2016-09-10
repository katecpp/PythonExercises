#! python3
import random

def generateRandomArr(maxLength, valueMin, valueMax):
    length = random.randint(1, maxLength)
    return [random.randint(valueMin, valueMax) for _ in range(length)]

a = generateRandomArr(20, 0, 50)
b = generateRandomArr(20, 0, 50)

print(a)
print(b)

commonElements = [x for x in set(a) if x in b]
print(commonElements)

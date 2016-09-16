#! python3
import random

def readInteger():
    value = ""
    while value.isdigit() == False:
        value = input("Which number you want to find? ")
        if value.isdigit() == False:
            print("This is not a number!")
    return int(value)

def createRandomOrderedList(minValue, maxValue, length):
    randArr = [random.randint(minValue, maxValue) for _ in range(0, length)]
    return sorted(randArr)

def binarySearch(array, value):
    leftIndex = 0
    rightIndex = len(array) - 1
    while rightIndex >= leftIndex:
        midIndex = (leftIndex + rightIndex)//2
        if array[midIndex] == value:
            return True
        elif array[midIndex] > value:
            rightIndex = midIndex - 1
        else:
            leftIndex = midIndex + 1
    return False

if __name__=="__main__":
    arr = createRandomOrderedList(0, 100, 10)
    print(arr)
    numberToFind = readInteger()
    print(binarySearch(arr, numberToFind))


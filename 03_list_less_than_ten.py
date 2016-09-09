#! python3
initialArray = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def readInteger(name):
    value = ""
    while value.isdigit() == False:
        value = input("Enter " + name + " : ")
        if value.isdigit() == False:
            print("This is not a number!")
    return int(value)

def filterArray(array, lessThan):
    filteredArray = [val for val in array if val < lessThan]
    return filteredArray

threshold = readInteger("threshold")
filteredArray = filterArray(initialArray, threshold)
print(filteredArray)

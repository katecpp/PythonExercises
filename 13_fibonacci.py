#! python3

def readInteger():
    value = ""
    while value.isdigit() == False:
        value = input("How many fibonacci numbers do you want?\n")
        if value.isdigit() == False:
            print("This is not a number!")
    return int(value)

def fibonacci(val):
    if val == 0 or val == 1:
        return 1
    else:
        return fibonacci(val-1) + fibonacci(val-2)

def fibSeq(maxValue):
    return [fibonacci(x) for x in range(0, maxValue)]

len = readInteger()
print(fibSeq(len))

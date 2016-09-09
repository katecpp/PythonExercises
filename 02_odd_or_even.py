#! python3

def readInteger(name):
    value = ""
    while value.isdigit() == False:
        value = input("Enter " + name + " : ")
        if value.isdigit() == False:
            print("This is not a number!")
    return int(value)


print("Check if NUM is divisible by DIV.\n")
num = readInteger("num")
div = readInteger("div")

if (div != 0 and num % div == 0):
    print(str(num) + " is divisible by " + str(div))
else:
    print(str(num) + " is not divisible by " + str(div))

#! python3

def readInteger(name):
    value = ""
    while value.isdigit() == False:
        value = input("Enter " + name + " : ")
        if value.isdigit() == False:
            print("This is not a number!")
    return int(value)

print("Divisor finder. What number you want to check?")
number = readInteger("number")
divisors = [x for x in range(1, number + 1) if number % x == 0]
print("The divisors of " + str(number) + " are: " + str(divisors))

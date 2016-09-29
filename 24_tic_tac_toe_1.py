#! python3

def readInteger():
    value = ""
    while value.isdigit() == False:
        value = input("The size of the board: ")
        if value.isdigit() == False:
            print("This is not a number!")
    return int(value)

def printHorizontal(size):
    print(size * " ---")

def printVertical(size):
    print((size + 1) * "|   ")

def drawBoard(size):
    for i in range(size):
        printHorizontal(size)
        printVertical(size)
    printHorizontal(size)

if __name__=="__main__":
    size = readInteger()
    drawBoard(size)

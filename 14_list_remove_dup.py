#! python3

def remDupWithSet(inList):
    inList = list(set(inList))
    return inList

def remDupWithLoop(inList):
    outList = []
    for x in inList:
        if x not in outList:
            outList.append(x)
    return outList

a = [1, 2, 3, 1, 2, 3]
print(remDupWithSet(a))
print(remDupWithLoop(a))


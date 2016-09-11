#! python3

def listBoundValues(listIn):
    return [listIn[0], listIn[-1]]

a = [5, 10, 15, 20, 25]

print(listBoundValues(a))

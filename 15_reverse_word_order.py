#! python3

def reverse(inString):
    wordList = inString.split()
    wordList.reverse()
    return " ".join(wordList)

inString = str(raw_input("Write a long string:\n"))
reversed = reverse(inString)
print(reversed)

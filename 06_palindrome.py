#! python3

# Extended slices explained here 
# https://docs.python.org/release/2.3.5/whatsnew/section-slices.html
def checkIfPalindrome(inStr):
    return inStr == inStr[::-1]

string = input("Type the string to check if it's palindrome\n")
print(string + (" is " if checkIfPalindrome(string) else " is not ") + "a palindrome.")

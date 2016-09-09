#! python3
import datetime

name = input("Give me your name: ")
age = int(input("Enter your age: "))
currentYear = datetime.datetime.now().year
year = 100 + currentYear - age
numberOfCopies = int(input("How many messages do you want? "))

print(numberOfCopies * (name + ", you will turn 100 years old in " + str(year) + " year.\n"))

# Exercise 0: Code Self-Check
# Alexander Birrell
# This program prints out the square roots of the numbers 1 to 1000, inclusive
from math import sqrt

def printSquareRoots():
    currentNumber = 1
    while currentNumber <= 1000:
        print(sqrt(currentNumber))
        currentNumber = currentNumber + 1


printSquareRoots()
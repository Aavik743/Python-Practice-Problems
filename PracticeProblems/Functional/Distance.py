""" A program that takes two integer command-line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0) """

from math import sqrt


def getDistance(x, y):  # function to compute the distance
    distance = sqrt(x * x + y * y)  # computation
    print("The distance is ", distance)


# Driver Code
x = int(input("Enter the value of X: "))  # user inputs
y = int(input("Enter the value of Y: "))
getDistance(x, y)  # function calling

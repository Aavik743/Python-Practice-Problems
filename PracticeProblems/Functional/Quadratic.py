""" A program to find the roots of given quadratic equation """
from cmath import sqrt


def getRoots(a, b, c):  # function to compute the roots
    delta = b * b - 4 * a * c
    root1 = -b + (sqrt(delta)) / (2 * a)
    root2 = -b - (sqrt(delta)) / (2 * a)
    print("The required roots are", root1, " & ", root2)


# Driver Code
x = int(input("Enter the value of a: "))  # user inputs
y = int(input("Enter the value of b: "))
z = int(input("Enter the value of c: "))
getRoots(x, y, z)  # function calling

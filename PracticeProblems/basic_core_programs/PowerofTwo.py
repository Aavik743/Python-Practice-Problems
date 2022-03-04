"""This program takes a command-line argument N and prints a table of the
powers of 2 that are less than or equal to 2^N"""

power = int(input("Enter a number between 0 to 30:\n "))  # Reading User Input

if power < 0:  # Checking for non-negative Input
    print("Provide a valid input")
elif power == 0:  # checking if power is 0
    print("2^0 = 1")
elif power <= 30: # checking for given condition
    for i in range(0, power + 1):  # Iterating till the user input
        value = 2 ** i  # calculating power of two
        print("2^", i, " = ", value)  # printing the output
else:
    print("Provide a valid input")  # Error statement

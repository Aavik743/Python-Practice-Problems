
""" A program to take a four digit input and check if it is a leap year """

import re

year = int(input("Enter the year you want to check: "))  # Reading User Input
try:
    if re.match("[0-9]{4}", year):   # Validating to match the given condition with regex

        if (year % 400 == 0) and (year % 100 == 0):  # leap yer condition
            print("{0} is a leap year".format(year))
        elif (year % 4 == 0) and (year % 100 != 0):  # leap yer condition
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))  # Printing the final statement
except Exception as e:
    print("Enter a proper year")  # to handle improper input

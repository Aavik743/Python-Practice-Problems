
""" Program to user input and replace the string template"""

import re

name = input("Enter your name: ")  # Takes input

if re.match("[A-Za-z]{3,}", name):  # Regex pattern to check if the input is proper
    print("Hello " + name + ", how are you?")
else:
    print("Please enter a proper name")

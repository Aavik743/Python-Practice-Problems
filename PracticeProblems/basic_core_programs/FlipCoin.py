
""" A program to take a number as input and toss a coin accordingly and return the heads and tails percentage """


import random

head_count = 0
tail_count = 0
count = 0
list = [1, 2]  # initiated variables

flips = int(input("No. of time you want the coin to be flipped: "))  # user input

while count < flips:    # loop to flip coin for given number of times
    toss = random.choice(list)
    if toss == 1:
        head_count += 1
        count += 1
    else:
        tail_count += 1
        count += 1

head_percentage = (head_count / flips) * 100  # Calculating heads percentage
tail_percentage = (tail_count / flips) * 100  # Calculating tails percentage

print("Total head count is: ", head_count, " and percentage of head is: ", head_percentage, "%")
print("Total tail count is: ", tail_count, " and percentage of count is: ", tail_percentage, "%")
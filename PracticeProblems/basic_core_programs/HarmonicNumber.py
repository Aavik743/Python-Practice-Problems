"""This program prints the Nth harmonic value: 1/1 + 1/2 + ... + 1/N"""

num = int(input("Enter a Nth number of the harmonic series: "))  # Read User Input
harmonic = 0

if num <= 0:
    print("Enter a positive number")  # Error statement
else:
    for i in range(1, num + 1):  # Iterating for number of times
        harmonic = harmonic + (1/i)  # Computation
print("the harmonic value of ", num, " is", harmonic)  # Printing result


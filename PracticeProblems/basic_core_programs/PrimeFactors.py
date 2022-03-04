"""This program prints the prime factors of any given number"""

num = int(input("Enter the number to check it's prime factors: "))  # Reading User Input
temp = num
i = 2
if temp <= 0:  # Checking for non-negative Input
    print("Enter a positive number")
elif temp == 1:
    print("1 doesn't have any prime factor")
else:
    while temp > 1:
        if temp % i == 0:  
            print(i, end=",")
            temp = int(temp // i)
        else:
            i += 1

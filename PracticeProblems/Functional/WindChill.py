""" A program  that takes two inputs temperature
and wind-speed and prints the wind chill """


def getWindChill(t, v):  # function to compute the wind chill
    w = 35.74 + (0.6215 * t) + ((0.4275 * t) - 35.75) * (v ** 0.16)
    print("The wind chill is ", w)


# Driver Code
t = int(input("Enter the temperature (less than 50): "))  # user inputs
v = int(input("Enter the wind speed (3 < v > 120): "))
getWindChill(t, v)  # function calling

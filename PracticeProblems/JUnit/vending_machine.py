"""Program to find the Fewest Notes to be returned for Vending Machine"""


def countCurrency(amount):  # Function to count notes and print the same
    total_amount = 0
    notes = [2000, 500, 200, 100, 50, 20, 10, 5, 1]  # total list of currency notes
    note_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # number of notes
    print("Currency notes list are: ")

    for i, j in zip(notes, note_counter):  # Greedy approach method
        if amount >= i:  # Zip function to compare total list of currency notes and number of notes
            j = amount // i
            amount = amount - j * i
            print(i, " : ", j)
            total = i * j
            total_amount += total
    return total_amount


amount = 5432  # Can take User input

if amount > 0:  # Validating if the entered is non-negative input
    countCurrency(amount)  # Function calling
else:
    print("Invalid Input!")  # Error message

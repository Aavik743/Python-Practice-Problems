""" A program to create library for reading in 2D arrays of integers, doubles, or booleans from
standard input and printing them out to standard output """

rows = int(input("Enter the no. of rows: "))  # take input for number of rows
columns = int(input("Enter the no. of columns: "))  # take input for number of columns

a = []

for i in range(rows):
    b = []
    for j in range(columns):
        elements = input("Enter the elements of the 2D Array: ")  # take input for the elements
        b.append(elements)  # add elements to 'b'
    a.append(b)  # add 'b' to 'a'
print(a)  # print the output

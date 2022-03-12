def findNumber(high, low=0):
    mid = (low + high) // 2

    print("Enter your choice below: ")
    print("1) Number greater than ", mid)
    print("2) Number less than ", mid)
    print("3) None of the above ")
    choice = str(input())

    if choice == '1':
        findNumber(high, mid)
        return

    elif choice == '2':
        findNumber(mid, low)
        return

    elif choice == '3':
        print("Got the guessed number: ", mid)
        return

    else:
        print("Invalid selection!")


# Driver code
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print('"Please select any number and remember in mind"')
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

high = int(input("Enter the upper range : \n"))

findNumber(high)

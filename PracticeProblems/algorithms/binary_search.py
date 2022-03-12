def binarySearch(array, start, end, word):
    sorted_array = sorted(array)

    if end >= start:
        mid = int((start + end) / 2)
        if sorted_array[mid] == word:
            return mid
        elif sorted_array[mid] > word:
            end = mid
            return binarySearch(array, start, end, word)
        else:
            start = mid
            return binarySearch(array, start, end, word)
    else:
        return -1


if __name__ == '__main__':
    array = ['cat', 'dog', 'bird', 'fish', 'elephant', 'horse', 'tiger', 'lion']
    print("Array is: ", array)
    start = 0  # Variables
    end = len(array) - 1

    word = str(input("Enter the word to be searched in the array: \n"))
    result = binarySearch(array, start, end, word)

    if result != -1:
        print("Array after sorted: ", sorted(array))
        print("Entered word-", word, " is present at index ", int(result))
    else:
        print("Entered word-", word, " is not present in array")

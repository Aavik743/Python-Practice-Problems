def mergeSort(arr):  # Function to perform merge sorting operation
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left = arr[:mid]  # Dividing the array elements
        right = arr[mid:]  # into 2 halves
        mergeSort(left)  # Sorting the first half
        mergeSort(right)  # Sorting the second half

        i = j = k = 0

        while i < len(left) and j < len(right):  # Copy data to temp arrays L[] and R[]
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):  # Checking if any element was left
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def printList(arr):  # Function to print the list
    for i in range(len(array)):  # Traversing till the array length
        print(array[i], end=" ")
    print()


if __name__ == '__main__':

    array = [2, 7, 5, 8, 3, 4]  # Array list
    print("Given array is", end="\n")
    printList(array)  # Function calling

    mergeSort(array)  # Function calling
    print("Sorted array is: ", end="\n")
    printList(array)  # Function calling

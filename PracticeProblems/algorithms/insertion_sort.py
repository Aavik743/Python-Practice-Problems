def insertion_sort(arr):
    print("We have: ", arr)
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j = j - 1
    print("After sorting: ", arr)


if __name__ == '__main__':
    alley = [2, 7, 5, 8, 3, 4]
    insertion_sort(alley)

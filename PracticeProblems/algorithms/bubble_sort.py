def bubble_sort(arr):
    print("We have: ", arr)
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    print("After sorting: ", arr)


if __name__ == '__main__':
    alley = [2, 7, 5, 8, 3, 4]
    bubble_sort(alley)

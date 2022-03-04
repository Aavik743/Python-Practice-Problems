""" A program with cubic running time to read in N integers and counts the number of triplets that sum to exactly 0 """


def getTriplets(arr, n):
    if n >= 3:
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if arr[i] + arr[j] + arr[k] == 0:
                        print(arr[i], ", ", arr[j], ", ", arr[k])

    else:
        print("Triplets not found")


# Driver Code
arr = [0, 1, -1, 2, -2, 3, -3]
n = len(arr)
getTriplets(arr, n)

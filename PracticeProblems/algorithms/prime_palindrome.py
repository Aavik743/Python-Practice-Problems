def get_primes(start, end):
    nums = []
    for i in range(start, end + 1):  # Traverse each number in the interval
        if i == 1:  # Skip 1 as 1 is neither prime nor composite
            continue
        flag = 1  # flag variable to tell if i is prime or not

        for j in range(2, i // 2 + 1):
            if i % j == 0:
                flag = 0
                break

        if flag == 1:  # flag = 1 means i is prime and flag = 0 means i is not prime
            nums.append(i)
    print("The prime numbers between", start, "and", end, " is ", nums)
    return nums


def check_palindrome(liist):
    palindrome = []
    for i in range(len(liist)):
        number = liist[i]
        temp_number = number
        reverse = 0

        while temp_number > 0:  # Traverse each number in the interval
            remainder = temp_number % 10
            reverse = (reverse * 10) + remainder
            temp_number = temp_number // 10
        if number == reverse:
            palindrome.append(number)
    return palindrome


if __name__ == '__main__':
    print("Enter lower(first) element of the interval: ")  # Ask user to enter lower value of interval
    start = int(input())  # Take input

    print("Enter upper(last) element of the interval: ")  # Ask user to enter upper value of interval
    end = int(input())  # Take input

    nums = get_primes(start, end)

    palindrome_list = check_palindrome(nums)
    print('The palindromes are', palindrome_list)
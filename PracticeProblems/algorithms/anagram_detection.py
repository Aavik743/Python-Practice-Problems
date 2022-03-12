def detect_anagram(str_a, str_b):
    strA = list(str_a)
    strB = list(str_b)

    check_a = all(item in strA for item in strB)
    check_b = all(item in strB for item in strA)

    if check_a == check_b == True:
        print("The two strings are anagram")
    else:
        print("The two strings are not anagram")


if __name__ == '__main__':
    str1 = 'earth'
    str2 = 'heart'
    detect_anagram(str1, str2)

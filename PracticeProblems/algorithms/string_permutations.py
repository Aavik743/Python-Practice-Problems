def get_permutation(string, i=0):
    if i == len(string):
        print(string)

    for j in range(i, len(string)):
        words = [c for c in string]

        words[i], words[j] = words[j], words[i]

        get_permutation(words, i+1)


if __name__ == '__main__':
    word = str(input("Enter a string: \n"))
    get_permutation(word)

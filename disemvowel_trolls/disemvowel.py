def main():
    print(disemvowel('This website is for losers LOL!'))


def disemvowel(string):
    vowels_list = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    for vowel in vowels_list:
        string = string.replace(vowel, '')
    return string


if __name__ == '__main__':
    main()
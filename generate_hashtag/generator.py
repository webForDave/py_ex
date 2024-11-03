def main():
    print(generate_hashtag('# welcome to this kata'))
        

def generate_hashtag(s):
    s_as_list = s.split(' ')
    s_as_list.insert(0, '#')
    words_list = []

    for word in s_as_list:
        words_list.append(word.title())

    new_s = ''.join(words_list)
    if len(new_s) > 140 or new_s == '' or (new_s == '#' and len(new_s) == 1):
        return False
    else:
        return new_s


if __name__ == '__main__':
    main()
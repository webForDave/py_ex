def main():
    print(duplicate_encode('JXX)dAQPGPm'))


def duplicate_encode(word):
    word_lower = word.lower()
    chars_count = {}

    for char in word_lower:
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1
    result = ''
    for char in word_lower:
        if chars_count[char] > 1:
            result += ')'
        else:
            result += '('
    return result




if __name__ == '__main__':
    main()
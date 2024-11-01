def main():
    print(high_and_low('1 2 -3 4 5'))


def high_and_low(numbers):
    numbers = numbers.split(' ')
    numbers_list = []
    for i in numbers:
        numbers_list.append(int(i))
        max_and_min = map(str, [max(numbers_list), min(numbers_list)])
    return ' '.join(max_and_min)


if __name__ == "__main__":
    main()
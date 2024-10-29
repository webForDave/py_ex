def main():
    print(square(65))


def square(num):
    squared_nums = []
    for i in str(num):
        squared_nums.append(int(i) * int(i))
        new_squared_nums = ''.join(map(str, squared_nums))
    return int(new_squared_nums)


if __name__ == '__main__':
    main()
def main():
    print(get_sum(3, 3))


def get_sum(a,b):
    numbers_list = []
    for i in range(a, b+1):
        numbers_list.append(i)
    if b == a:
        return a
    else:
        return sum(numbers_list)


if __name__ == '__main__':
    main()
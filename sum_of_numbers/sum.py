def main():
    print(get_sum(-2, 3))


def get_sum(a,b):
    # return sum(range(a, b+1))
    nums_list = []
    for i in range(a, b+1):
        nums_list.append(i)
    return sum(nums_list)


if __name__ == '__main__':
    main()
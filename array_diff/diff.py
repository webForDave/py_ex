def main():
    print(array_diff([1,2,2,2,3],[2]))


def array_diff(a, b):
    return [i for i in a if i not in b]

if __name__ == '__main__':
    main()
def main():
    print(array_diff([1,2,2,2,3],[2]))


def array_diff(a, b):
    new_list = [i for i in a if i not in b]
    return new_list

if __name__ == '__main__':
    main()
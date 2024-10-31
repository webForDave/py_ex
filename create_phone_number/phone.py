def main():
    print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))


def create_phone_number(n):
    if len(n) == 10:
        n = ''.join(map(str, n))
        prefix = n[0:3]
        middle = n[3:6]
        suffix = n[6:]
        return f"({prefix}) {middle}-{suffix}"
    else:
        return 0



if __name__ == '__main__':
    main()
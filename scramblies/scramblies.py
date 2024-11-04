def main():
    print(scramble('festqrwpdgpl', 'tpsqdqew'))


def scramble(str1, str2):
    new_list = []
    for i in str2:
        if i in str1:
            new_list.append(True)
        else:
            new_list.append(False)
    if False in new_list:
        return False
    else:
        return True


if __name__ == '__main__':
    main()
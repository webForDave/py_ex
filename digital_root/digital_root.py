def main():
    print(digital_root(942))


def digital_root(n):
    while True:
        n_str = str(n)
        new_list = []
        for i in n_str:
            new_list.append(int(i))
        new_num = str(sum(new_list))
        if len(new_num) != 1:
            continue
        else: 
            return int(new_num)


if __name__ == '__main__':
    main()
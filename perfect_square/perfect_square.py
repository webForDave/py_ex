def main():
    print(find_next_square(625))


def find_next_square(sq):
    sq = sq ** (1/2)
    if sq == int(sq):
        sq = sq + 1
        return int(sq * sq)
    else:
        return -1


if __name__ == '__main__':
    main()
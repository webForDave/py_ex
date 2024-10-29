def main():
    print(friend(["Ryan", "Kieran", "Jason", "Yous"]))


def friend(x):
    friends = []
    for friend in x:
        if len(friend) == 4:
            friends.append(friend)
    return friends


if __name__ == '__main__':
    main()
def main():
    print(count_smileys([':$']))


def count_smileys(arr):
    smileys = [':)', ';D', ':-D', ':D', ';-D', ':~)', ';~D']
    count = 0
    for i in arr:
        if i in smileys:
            count += 1
    return count



if __name__ == '__main__':
    main()
def main():
    print(maskify('12345678910'))


def maskify(cc):
    new_digits = []
    last_digits = cc[-4:]
    n = 4
    for i in cc:
        new_digits.append(i)

    del new_digits[-4:]
    new_digits = ''.join(new_digits)

    for j in new_digits:
        new_digits = new_digits.replace(j, '#')

    new_digits = list(new_digits)
    new_digits.append(last_digits)
    
    return ''.join(new_digits)

if __name__ == '__main__':
    main()

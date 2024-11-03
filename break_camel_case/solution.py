def main():
    print(solution('identiFier'))


def solution(s):
    for i in s:
        if i == i.upper():
            s = s.replace(i.upper(), f' {i}')
    return s.strip()


if __name__ == '__main__':
    main()
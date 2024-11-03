def main():
    print(solution('breakCamel  Case'))


def solution(s):
    new_str = s.replace(' ', '')
    result = []
    for i in new_str:
        if i == i.upper():
            result.append(' ')
        result.append(i)
    return ''.join(result).strip()



if __name__ == '__main__':
    main()
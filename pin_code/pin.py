def main():
    print(validate_pin('0000'))

def validate_pin(pin):
    if pin.isdigit():
        if len(pin) == 4 or len(pin) == 6:
            return True
        else:
            return False 
    else:
        return False


if __name__ == '__main__':
    main()

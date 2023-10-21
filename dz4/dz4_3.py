def f(x):
    if len(x) == len(set(x)):
        return True
    else:
        return False


if __name__ == '__main__':
    print(f(input("введите строку:")))

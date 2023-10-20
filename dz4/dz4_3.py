def f(x):
    if len(x) == len(set(x)):
        return True
    else:
        return False

x = input("Введите строку: ")
print(f(x))

if __name__ == '__main__':
    print(f(input()))

def f():
    n = int(input())
    if n > 1:
        f = 1
        while n > 1:
            f = f * n
            n = n - 1
        return f
    elif n == 0 or n == 1:
        return 1
    else:
        return "не существует"
print(f())


if __name__ == "__main__":
    print(f(int(input())))
def f(n):
    x = []
    while n:
        x.append(n)
        n = input("Список: ")
    return x

def func(x, b):
    b %= len(x)
    return x[-b:] + x[:-b]

if __name__ == "__main__":
    b = int(input("k: "))
    n = input("Список: ")
    c = 0
    x = f(n)
    print(func(x, b))
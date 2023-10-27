def func(x):
    y = set()
    for i in x:
        if i in y:
            return False
        y.add(i)
    return True


if __name__ == "__main__":
    print(func(input()))
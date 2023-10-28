def f(a):
    x = []
    while a:
        x.append(a)
        a = input()
    return x


def func(k, pos):
    k = k % len(pos)
    pos = pos[-k:] + pos[:-k]
    return pos  

if __name__ == '__main__':
    print(func(int(input()), f(int(input()))))
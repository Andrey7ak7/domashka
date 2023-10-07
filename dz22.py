a, b = input("введите число:"), []
while a:
    b.append(a)
    a = input()

b.sort(reverse=True)
print(''.join(b))
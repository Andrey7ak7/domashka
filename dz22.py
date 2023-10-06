a, b = input("введите число:"), ["наибольшее:"]
while a:
    b.append(a)
    a = input()

b.sort(reverse=True)
print(''.join(b))
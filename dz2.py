a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
d = float(input("d="))
f = float(input("f="))
if f - d != 0:
    mag = (a * b - c) / (f - d)
    print(mag)
else:
    print("деление на 0!!!")
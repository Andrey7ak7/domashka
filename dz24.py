a = input()
o, z = a.count('('), a.count(')')

if o > z:
    print(f'Не хватает {o - z} закрывающихся скобок!')
elif z > o:
    print(f"Не хватает {z - o} открывающихся скобок!")
else:
    print("Всё нормально,молодец)")
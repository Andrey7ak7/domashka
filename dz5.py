x = float(input("введите координаты x-"))
y = float(input("введите координаты y-"))
if x > 0 and y > 0:
    print("1 четверть")
elif x > 0 and y < 0:
    print("4 четверть")
elif x < 0 and y > 0:
    print("2 четверть")
elif x < 0 and y < 0:
    print("3 четверть")
else:
    print("точка лежит на оси")
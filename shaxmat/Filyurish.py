x = int(input("x ni kiriting="))
y = int(input("y ni kiriting="))
d1 = min(x - 1, y - 1)
d2 = min(8 - x, 8 - y)
D1 = min(8 - x, y - 1)
D2 = min(x - 1, 8 - y)
g= d1+d2+D1+D2

print("yurishlar soni=",g)

# otning kordinatalari:
x1, y1 = map(int, input("1-otning kordinatasi=").split())
x2, y2 = map(int, input("2-otning kordinatasi=").split())
if (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2):
    print(True)
else:
    print(False)

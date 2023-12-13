from random import randint
class Hetman:
    def __init__(self, r, c):
        self.r = r
        self.c = c
n = int(input("Podaj ilość Hetmanów: "))
data = []
for i in range(n):
    x = int(input("Podaj wartość " + str(i + 1) + "-ego rzędu dla Hetmana: "))
    y = int(input("Podaj wartość " + str(i + 1) + "-ej kolumny dla Hetmana: "))
    sthg = Hetman(x, y)
    a = sthg.r
    b = sthg.c
    data.append((a, b))


r = []
c = []

for i in data:
    r.append(i[0])
    c.append(i[1])
d1, d2 = [], []
n = len(r)

for i in range(n):
    d1.append(r[i] + c[i])
    d2.append(r[i] - c[i] + 100)


def equality(x):
    n = len(x)
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j]:
                return True
    return False


if equality(r) or equality(c) or equality(d1) or equality(d2):
    print("Hetmany się szachują")
else:
    print("Hetmany się nie szachują")

with open("text2.txt", "w") as f:
    chessboard = []
    for i in range(10001):
        chessboard.append("[ ]")
    for i in data:
        y = 100 * (i[0] - 1) + i[1] - 1
        chessboard[y] = "[H]"
    for j in range(0, 100):
        for i in range(100*j, 100*(j + 1)):
            f.write(chessboard[i])
        f.write("\n")
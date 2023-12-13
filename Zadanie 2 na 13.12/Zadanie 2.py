from random import randint
auto = str(input('Wpisz "T", jeśli chcesz automatycznie wygenerować Hetmany oraz ich położenie, wpisz "N" żeby ręcznie ustawić ilość i ich pozycję: '))
auto.upper()
data = []

if auto == "T":
    n = randint(2, 100)
    for i in range(n):
        row = randint(1, 100)
        column = randint(1, 100)
        data.append((row, column))

else:
    h_amount = int(input("Podaj ilość hetmanów: "))
    for i in range(h_amount):
        row = int(input("Podaj liczbę wiersza: "))
        column = int(input("Podaj liczbę rzędu: "))
        data.append((row, column))
print(data)
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


chessboard = []
for i in range(10001):
    chessboard.append("[ ]")
for i in data:
    y = 100 * (i[0] - 1) + i[1] - 1
    chessboard[y] = "[H]"
for j in range(0, 100):
        print(chessboard[0 + 100 * j], chessboard[1 + 100 * j], chessboard[2 + 100 * j], chessboard[3 + 100 * j], chessboard[4 + 100 * j], chessboard[5 + 100 * j], chessboard[6 + 100 * j], chessboard[7 + 100 * j], chessboard[8 + 100 * j], chessboard[9 + 100 * j], chessboard[10 + 100 * j], chessboard[11 + 100 * j], chessboard[12 + 100 * j], chessboard[13 + 100 * j], chessboard[14 + 100 * j], chessboard[15 + 100 * j], chessboard[16 + 100 * j], chessboard[17 + 100 * j], chessboard[18 + 100 * j], chessboard[19 + 100 * j], chessboard[20 + 100 * j], chessboard[21 + 100 * j], chessboard[22 + 100 * j], chessboard[23 + 100 * j], chessboard[24 + 100 * j], chessboard[25 + 100 * j], chessboard[26 + 100 * j], chessboard[27 + 100 * j], chessboard[28 + 100 * j], chessboard[29 + 100 * j], chessboard[30 + 100 * j], chessboard[31 + 100 * j], chessboard[32 + 100 * j], chessboard[33 + 100 * j], chessboard[34 + 100 * j], chessboard[35 + 100 * j], chessboard[36 + 100 * j], chessboard[37 + 100 * j], chessboard[38 + 100 * j], chessboard[39 + 100 * j], chessboard[40 + 100 * j], chessboard[41 + 100 * j], chessboard[42 + 100 * j], chessboard[43 + 100 * j], chessboard[44 + 100 * j], chessboard[45 + 100 * j], chessboard[46 + 100 * j], chessboard[47 + 100 * j], chessboard[48 + 100 * j], chessboard[49 + 100 * j], chessboard[50 + 100 * j], chessboard[51 + 100 * j], chessboard[52 + 100 * j], chessboard[53 + 100 * j], chessboard[54 + 100 * j], chessboard[55 + 100 * j], chessboard[56 + 100 * j], chessboard[57 + 100 * j], chessboard[58 + 100 * j], chessboard[59 + 100 * j], chessboard[60 + 100 * j], chessboard[61 + 100 * j], chessboard[62 + 100 * j], chessboard[63 + 100 * j], chessboard[64 + 100 * j], chessboard[65 + 100 * j], chessboard[66 + 100 * j], chessboard[67 + 100 * j], chessboard[68 + 100 * j], chessboard[69 + 100 * j], chessboard[70 + 100 * j], chessboard[71 + 100 * j], chessboard[72 + 100 * j], chessboard[73 + 100 * j], chessboard[74 + 100 * j], chessboard[75 + 100 * j], chessboard[76 + 100 * j], chessboard[77 + 100 * j], chessboard[78 + 100 * j], chessboard[79 + 100 * j], chessboard[80 + 100 * j], chessboard[81 + 100 * j], chessboard[82 + 100 * j], chessboard[83 + 100 * j], chessboard[84 + 100 * j], chessboard[85 + 100 * j], chessboard[86 + 100 * j], chessboard[87 + 100 * j], chessboard[88 + 100 * j], chessboard[89 + 100 * j], chessboard[90 + 100 * j], chessboard[91 + 100 * j], chessboard[92 + 100 * j], chessboard[93 + 100 * j], chessboard[94 + 100 * j], chessboard[95 + 100 * j], chessboard[96 + 100 * j], chessboard[97 + 100 * j], chessboard[98 + 100 * j], chessboard[99 + 100 * j], chessboard[100 + 100 * j])



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

with open("text1.txt", "w") as f:
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


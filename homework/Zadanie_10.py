from random import randint

print("Witaj w kalkulatorze, podaj dwie cyfry aby wykonać działania")
while True:
    dzialanie = str(input("Podaj działanie jakie chcesz wykonać z 6 dostępnych ( + , - , * , / , # , ^ , x ): "))
    #if str(dzialanie) == "+" or str(dzialanie) == "-" or str(dzialanie) == "*" or str(dzialanie) == "/" or str(dzialanie) == "^" or str(dzialanie) == "#":
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))

    if str(dzialanie) == "+":
        print("Wynik sumy twoich liczb wynosi: ", a + b)

    if str(dzialanie) == "-":
        print("Wynik różnicy twoich liczb wynosi: ", a - b)

    if str(dzialanie) == "*":
        print("Wynik iloczynu twoich liczb wynosi: ", a * b)

    if str(dzialanie) == "/":
        print("Wynik dzielenia twoich liczb wynosi: ", a / b)

    if str(dzialanie) == "^":
        print("Wynik potęgowania pierwszej liczby do drugiej wynosi: ", a ** b)

    if str(dzialanie) == "#":
        print("Pierwiastek wybranej potęgi z pierwszej liczby wynosi: ", a ** (1 / b))

    if str(dzialanie) == "x":
        los = randint(a, b)
        print("Losowa liczba z danego przedziału wynosi: ", los)
    n = str(input("Czy chcesz skoończyć z używania kalkulatora? (T/N): "))
    if str(n) == "T":
        break




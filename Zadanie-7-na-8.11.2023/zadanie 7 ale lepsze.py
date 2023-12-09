m = int(input("Podaj liczbę aby wyznaczyć zakres silni: "))

def silnia(m):
    s = 1
    for i in range(2, m + 1):
        s *= i
    return s

#Podanie definicji silnii

if m >= 0:

    if m <100:
        for i in range(1, m + 1):
            print("Wynik silnii: ", silnia(i), "\nWynik odejmowania silni", i, "od silni", i-1, ":", silnia(i) - silnia(i - 1))

    else:
        for i in range(m - 50, m):
            print("Wynik silnii: ", silnia(i), "\nWynik odejmowania silni", i, "od silni", i - 1, ":", silnia(i) - silnia(i - 1))
        more = str(input('Czy chcesz zobaczyć więcej wyników silnii? "T" Tak, "N", Nie: '))
        ile = int(input("Ile silnii mniejszych od chcesz zobaczyć?"))
        more.upper()
        if (more == "T"):
            more = True
            n = 0
            while more:
                for i in range(m - 50 - ile * (n + 1), m - 50 - ile * n):
                    print("Wynik silnii: ", silnia(i), "\nWynik odejmowania silni", i, "od silni", i - 1, ":", silnia(i) - silnia(i - 1))
                more = str(input('Czy chcesz zobaczyć więcej wyników silnii? "T" Tak, "N", Nie: '))
                p= m - 50 - ile * (n + 1)
                more.upper()
                if more == "T":
                    more = True
                elif more == "N":
                    more = False
                    break
                else:
                    print("Error")
                ile = input('Ile silnii mniejszych od {n}'.format(n=p))
else:
    print("Błąd, podaj wartoś nieujemną.")

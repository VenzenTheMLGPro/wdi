m = int(input("Podaj liczbę aby wyznaczyć zakres silni: "))

def silnia(m):
    s = 1
    for i in range(2, m + 1):
        s *= i
    return s

#Podanie definicji silni

if m >= 0:
    for i in range(1, m + 1):
        print("Wynik silnii: ", silnia(i), "\nWynik odejmowania silni", i, "od silni", i-1, ":", silnia(i) - silnia(i)/i)
else:
    print("Błąd, podaj wartoś nieujemną.")




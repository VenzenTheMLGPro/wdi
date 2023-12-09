import math
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
if(a<0 or b<0):
    print("error liczba musi być większa od zera")
else:
    print("Suma liczb: ", a + b)
    print("Różnica liczb: ", a - b)
    print("Dzielenie liczb: ", a / b, "\nIloczyn liczb: ", a * b)
    print("Kwadrat liczby pierwszej: ", a**2, "\nPierwiastek liczby drugiej: ", b**2)
    print("Pierwiastek liczby pierwszej: ", math.sqrt(a), "\nPierwiastek liczby drugiej: ", math.sqrt(b))

import math
import cmath
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
if(a>0 and b>0):
    print("Suma liczb: ", a + b)
    print("Różnica liczb: ", a - b)
    print("Dzielenie liczb: ", a / b, "\nIloczyn liczb: ", a * b)
    print("Kwadrat liczby pierwszej: ", a**2, "\nPierwiastek liczby drugiej: ", b**2)
    print("Pierwiastek liczby pierwszej: ", math.sqrt(a), "\nPierwiastek liczby drugiej: ", math.sqrt(b))
elif(a<0 and b>0):
    c = abs(a)
    print("Suma liczb: ", c + b)
    print("Różnica liczb: ", c - b)
    print("Dzielenie liczb: ", c / b, "\nIloczyn liczb: ", c * b)
    print("Kwadrat liczby pierwszej: ", c**2, "\nPierwiastek liczby drugiej: ", b**2)
    print("Pierwiastek liczby pierwszej: ", math.sqrt(c), "\nPierwiastek liczby drugiej: ", math.sqrt(b))
elif (a > 0 and b < 0):
    d = abs(b)
    print("Suma liczb: ", a + d)
    print("Różnica liczb: ", a - d)
    print("Dzielenie liczb: ", a / d, "\nIloczyn liczb: ", d * a)
    print("Kwadrat liczby pierwszej: ", a ** 2, "\nPierwiastek liczby drugiej: ", d ** 2)
    print("Pierwiastek liczby pierwszej: ", math.sqrt(a), "\nPierwiastek liczby drugiej: ", math.sqrt(d))
else:
    print("Byczq nie mogę pierwiastkować liczb ujemnych, to że jedną wartośc ujemną przeoczyłem to nie znaczy że możesz dowolnie pierwiastkować liczby ujemne ;)")
if(a*b == 10 or c*b == 10 or a*d == 10):
    print("Yay!")
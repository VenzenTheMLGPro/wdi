from random import randint
a = int(input("Podaj liczbę zakresu dla losowania pewnej liczby: "))
for i in range(3):
    c = randint(1, a)
    print(c)

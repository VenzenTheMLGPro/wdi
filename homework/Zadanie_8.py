from random import randint
a = int(input("Podaj całkowitą liczbę nieujemną: "))
i = 0
print((a + 2) * " ", "X")
while i < a - 1:
    i += 1
    n = randint(2, 2 * i)
    print((a - i) * " ", ((2 * i) - n) * "*", "o", n * "*")
print((a + 2) * " ", "U")




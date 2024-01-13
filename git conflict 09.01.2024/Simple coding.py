from random import randint
a = int(input("Podaj górną liczbę zakresu dla losowanej liczby: "))
b = int(input("Podaj dolną liczbę zakresu dla losowanej liczby: "))
if a > b:
  c = randint(b, a)
  print(c)
if a < b:
  c = randint(a, b)
else:
  print(a)

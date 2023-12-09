#macierz X i Y oraz wynik
X = []
Y = []
wynik = []
#Wprowadzenie rządu i kolumny
rzad = int(input("Podaj liczbę rzędu: "))
kolumna = int(input("Podaj liczbę kolumn: "))
#rząd i kolumna musi być taka sama w przypadku sumy, dlatego tylko jedno zapytanie
#Pętla od 1 do ostatniego rzędu
for Rzad in range(rzad):
	a = []
	#Pętla od liczby 1 do ostatniej kolumny w wybranym rzędzie
	for Kolumna in range(kolumna):
		a.append(int(input("Podaj liczby w pierwszej macierzy")))
		#Dodaje do tablicy wszystkie liczby aż do uzupełnienia wiesza
	X.append(a)
	#Utworzenie macierzy poprzez sumę tablicy w tablicy

for Rzad in range(rzad):
	b = []
	for Kolumna in range(kolumna):
		b.append(int(input("Podaj liczby w drugiej macierzy")))
	Y.append(b)

for Rzad in range(rzad):
	c = []
	for Kolumna in range(kolumna):
		c.append(0)
	wynik.append(c)
#Adekwatnie jak wyżej

for Rzad in range(rzad):
	for Kolumna in range(kolumna):
		wynik[Rzad][Kolumna] = X[Rzad][Kolumna] + Y[Rzad][Kolumna]
#Suma odpowiedni wyrazów (np. wynik[1][1] = X[1][1] + Y[1][1]
print("Suma macierzy")
for w in wynik:
	print(w)

for Rzad in range(rzad):
	for Kolumna in range(kolumna):
		wynik[Rzad][Kolumna] = X[Rzad][Kolumna] - Y[Rzad][Kolumna]
#Adekwatnie jak przy sumie
print("Różnica macierzy")
for w in wynik:
	print(w)
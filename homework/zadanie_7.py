a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

if(a > b):
    while b < a:
        lista = [a]
        lista[a] = lista[a+1]
        if len(lista) < 20:
            for a in lista:
                print(a)
    else:
        j = int((a + b) / 2 - 3)
        if j < int(a+b/2 + 3):
            j += 1
            print(j)


elif(a <= b):
    while a <= b:
        lista = [a]
        lista[a] = lista[a + 1]
        if len(lista)< 20:
            print(lista)
        else:
            x = int((a + b) / 2 - 3)
            if x < int(a + b / 2 + 3):
                x += 1
                print(x)


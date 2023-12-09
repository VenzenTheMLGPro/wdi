a = int(input("Napisz dowolną liczbę, aby sprawdzić czy jest pierwsza:" ))
i = 0
for i in range(0, a):
    i+=1
    if(a%i == 0):
        print(int(a/i))
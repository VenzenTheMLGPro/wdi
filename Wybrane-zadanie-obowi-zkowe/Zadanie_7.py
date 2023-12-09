a = int(input("Napisz dowolną liczbę, aby sprawdzić jej dzielniki:" ))
i = 0
if(a>0 or a<0):
    for i in range(0, a):
        i+=1
        if(a%i == 0):
            print(int(a/i))
    for i in range(0, a):
        i+=1
        if(a%i == 0):
            print(int(-a/i))
elif(a==0):
    print("Zero ma nieskończenie wiele dzielników")
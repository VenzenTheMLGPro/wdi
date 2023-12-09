hajs = 0
pin = int(input("Podaj PIN:"))
while True:
    wprowadz_pin = int(input("Podaj swój PIN: "))
    if wprowadz_pin == pin:
        opcje = str(input('Co chcesz zrobić w kolejnym kroku? (Wypłata - "Wyp", Wpłata - "Wpł", Stan konta - "SK", Wyjście - "W") '))
#wypłata
        if str(opcje) == "Wyp":
            print("Obecny stan konta: ", hajs)
            wyplata = int(input("Podaj ile chcesz wypłacić z konta: "))
            if hajs - wyplata < 0:
                print("Wypłata niemożliwa, brak środków na koncie")
            else:
                hajs -= wyplata
                print("Obecny stan konta wynosi", hajs)
#wpłata
        if str(opcje) == "Wpł":
            wplata = int(input("Podaj ile chcesz wpłacić na konto: "))
            hajs += wplata
            print("Obecny stan konta wynosi: ", hajs)
#Sprawdzenie stanu konta
        if str(opcje) == "SK":
            print("Obecny stan konta wynosi: ", hajs)
#nieprawidlowy pin
        if str(opcje) == "W":
            break
    else:
        print("PIN nieprawidłowy, spróbuj ponownie")
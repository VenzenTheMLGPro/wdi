a = str(input("Podaj folder, który chcesz edytować: "))

with open(a, "r") as f: #dostęp do pliku poprzez program "r" służy do odczytu
    sentence = f.read() #sczytanie pliku
    separate = sentence.split(" ")
    print("Zdanie początkowe w pliku:\n", sentence)


#definicja funkcji dla samogłoski na początku i końcu słowa
def reverse_vowel2():

    for i in range(len(separate)):
        p = separate[i][0].lower()
        r = separate[i][-1].lower()
        vowel = ['a', 'o', 'i', 'y', 'u', 'e']

        if p in vowel and r in vowel:
            separate[i] = separate[i].upper()
            separate[i] = separate[i][::-1]
    return separate

#definicja funkcji dla samogłoski na początku słowa
def reverse():

    for i in range(len(separate)):
        p = separate[i][0].lower()
        r = separate[i][-1].lower()
        vowel = ['a', 'o', 'i', 'y', 'u', 'e']

        if p in vowel and r not in vowel:
            separate[i] = separate[i][::-1]
            separate[i] = separate[i].lower()
    return separate

with open(a, "w") as f: # otworzenie pliku i edycja poprzez nadpisanie "w"
    reverse()
    reverse_vowel2()
    outputstr = " ".join(separate)
    f.write(outputstr)

with open(a, "r") as f:
    print("Wynik końcowy w pliku:\n", f.read())




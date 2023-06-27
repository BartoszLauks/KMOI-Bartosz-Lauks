def szyfruj_cezar(tekst, przesuniecie):
    zaszyfrowany_tekst = ""
    for znak in tekst:
        if znak.isalpha():  # Sprawdza, czy znak jest literą
            if znak.isupper():  # Sprawdza, czy znak jest wielką literą
                kod = ord('A')
            else:
                kod = ord('a')
            przesuniety_kod = (ord(znak) - kod + przesuniecie) % 26 + kod
            zaszyfrowany_tekst += chr(przesuniety_kod)
        else:
            zaszyfrowany_tekst += znak
    return zaszyfrowany_tekst

def deszyfruj_cezar(tekst, przesuniecie):
    return szyfruj_cezar(tekst, -przesuniecie)

if __name__ == '__main__':

    # Przykładowe użycie
    tekst = "Hello, World!"
    przesuniecie = 3

    zaszyfrowany_tekst = szyfruj_cezar(tekst, przesuniecie)
    print("Zaszyfrowany tekst:", zaszyfrowany_tekst)

    odszyfrowany_tekst = deszyfruj_cezar(zaszyfrowany_tekst, przesuniecie)
    print("Odszyfrowany tekst:", odszyfrowany_tekst)

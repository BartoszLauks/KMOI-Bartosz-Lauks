import random


def generuj_klucz(alfabet):
    klucz = {}
    for litera, zaszyfrowane_litery in alfabet.items():
        if litera not in klucz:
            klucz[litera] = []
        klucz[litera].extend(zaszyfrowane_litery)
    return klucz


def szyfruj_homofonicznie(tekst_jawny, klucz):
    szyfrogram = ""
    for litera in tekst_jawny:
        if litera in klucz:
            zaszyfrowane_litery = klucz[litera]
            zaszyfrowana_litera = random.choice(zaszyfrowane_litery)
            szyfrogram += zaszyfrowana_litera
        else:
            szyfrogram += litera
    return szyfrogram


def deszyfruj_homofonicznie(szyfrogram, klucz):
    deszyfrowany_tekst = ""
    for litera in szyfrogram:
        for klucz_litera, klucz_wartosci in klucz.items():
            if litera in klucz_wartosci:
                deszyfrowany_tekst += klucz_litera
                break
        else:
            deszyfrowany_tekst += litera
    return deszyfrowany_tekst


alfabet = {
    'A': ['%', '$'],
    'B': ['#'],
    'C': ['@'],
    'D': ['&'],
    'E': ['^'],
    'F': ['*'],
    'G': ['!'],
    'H': ['~'],
    'I': [';', ':'],
    'J': ['<', '>'],
    'K': ['?', '/']
}

if __name__ == '__main__':
    klucz = generuj_klucz(alfabet)

    tekst_jawny = "Test szyfru"
    szyfrogram = szyfruj_homofonicznie(tekst_jawny, klucz)
    print("Szyfrogram:", szyfrogram)

    deszyfrowany_tekst = deszyfruj_homofonicznie(szyfrogram, klucz)
    print("Deszyfrowany tekst:", deszyfrowany_tekst)

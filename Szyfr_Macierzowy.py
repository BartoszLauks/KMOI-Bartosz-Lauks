def szyfr_maciezowy(slowo_klucz, tekst_jawny):
    slowo_klucz = slowo_klucz.lower().replace(" ", "")
    tekst_jawny = tekst_jawny.lower().replace(" ", "")

    klucz_dl = len(slowo_klucz)
    klucz_macierz = [[0] * klucz_dl for _ in range(klucz_dl)]
    poz = 0

    for i in range(klucz_dl):
        for j in range(klucz_dl):
            klucz_macierz[i][j] = ord(slowo_klucz[poz]) - 97
            poz = (poz + 1) % klucz_dl

    tekst_dl = len(tekst_jawny)
    tekst_macierz = [[0] * klucz_dl for _ in range((tekst_dl + klucz_dl - 1) // klucz_dl)]

    for i in range(tekst_dl):
        tekst_macierz[i // klucz_dl][i % klucz_dl] = ord(tekst_jawny[i]) - 97

    tekst_zaszyfrowany = ""

    for i in range((tekst_dl + klucz_dl - 1) // klucz_dl):
        for j in range(klucz_dl):
            suma = 0
            for k in range(klucz_dl):
                suma += klucz_macierz[j][k] * tekst_macierz[i][k]
            tekst_zaszyfrowany += chr((suma % 26) + 97)

    return tekst_zaszyfrowany

if __name__ == '__main__':

    slowo_klucz = "KLUCZ"
    tekst_jawny = "TO JEST TAJNY TEKST"

    zaszyfrowany_tekst = szyfr_maciezowy(slowo_klucz, tekst_jawny)
    print("Zaszyfrowany tekst:", zaszyfrowany_tekst)

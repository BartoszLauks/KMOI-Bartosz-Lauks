def szyfr_cmentarny(tekst):
    tekst = tekst.upper()
    szyfrogram = ""
    zamiana = {"A": "C", "B": "E", "C": "A", "D": "G", "E": "B", "F": "I",
               "G": "D", "H": "F", "I": "H", "J": "K", "K": "J", "L": "N",
               "M": "P", "N": "L", "O": "R", "P": "M", "Q": "T", "R": "O",
               "S": "V", "T": "Q", "U": "X", "V": "S", "W": "Z", "X": "U",
               "Y": "W", "Z": "Y"}

    for litera in tekst:
        if litera in zamiana:
            szyfrogram += zamiana[litera]
        else:
            szyfrogram += litera

    return szyfrogram


if __name__ == '__main__':
    tekst_jawny = "Moja wiadomość"
    szyfrogram = szyfr_cmentarny(tekst_jawny)
    print("Szyfrogram:", szyfrogram)

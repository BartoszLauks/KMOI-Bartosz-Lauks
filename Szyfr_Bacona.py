def szyfr_bacona(tekst):
    alfabet = {
        'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA',
        'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB',
        'K': 'ABABA', 'L': 'ABABB', 'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA',
        'P': 'ABBBB', 'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
        'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB', 'Y': 'BBAAA',
        'Z': 'BBAAB'
    }

    tekst = tekst.upper()
    szyfrogram = ""

    for litera in tekst:
        if litera in alfabet:
            szyfrogram += alfabet[litera]
        else:
            szyfrogram += litera

    return szyfrogram


def deszyfr_bacona(szyfrogram):
    alfabet = {
        'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D', 'AABAA': 'E',
        'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H', 'ABAAA': 'I', 'ABAAB': 'J',
        'ABABA': 'K', 'ABABB': 'L', 'ABBAA': 'M', 'ABBAB': 'N', 'ABBBA': 'O',
        'ABBBB': 'P', 'BAAAA': 'Q', 'BAAAB': 'R', 'BAABA': 'S', 'BAABB': 'T',
        'BABAA': 'U', 'BABAB': 'V', 'BABBA': 'W', 'BABBB': 'X', 'BBAAA': 'Y',
        'BBAAB': 'Z'
    }

    deszyfrowany_tekst = ""
    i = 0

    while i < len(szyfrogram):
        if szyfrogram[i] == ' ':
            deszyfrowany_tekst += ' '
            i += 1
            continue

        fragment = szyfrogram[i:i + 5]
        if fragment in alfabet:
            deszyfrowany_tekst += alfabet[fragment]
        else:
            deszyfrowany_tekst += fragment

        i += 5

    return deszyfrowany_tekst


if __name__ == '__main__':
    tekst_jawny = "Moja wiadomość"
    szyfrogram = szyfr_bacona(tekst_jawny)
    print("Szyfrogram:", szyfrogram)

    deszyfrowany_tekst = deszyfr_bacona(szyfrogram)
    print("Deszyfrowany tekst", deszyfrowany_tekst)

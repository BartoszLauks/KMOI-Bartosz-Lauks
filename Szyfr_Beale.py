import random


def generate_beale_cipher():
    # Tekst oryginalny
    original_text = """
    Four score and seven years ago our fathers brought forth on this continent, a new nation,
    conceived in Liberty, and dedicated to the proposition that all men are created equal.
    """

    # Usuwanie zbędnych znaków interpunkcyjnych i spacji
    cleaned_text = ''.join(c.lower() for c in original_text if c.isalpha())

    # Generowanie klucza szyfru
    key = [random.randint(1, 6) for _ in range(len(cleaned_text))]

    # Szyfrowanie
    cipher_text = ''
    for i, char in enumerate(cleaned_text):
        shift = key[i]
        cipher_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        cipher_text += cipher_char

    return key, cipher_text


def decrypt_beale_cipher(key, cipher_text):
    # Deszyfrowanie
    decrypted_text = ''
    for i, char in enumerate(cipher_text):
        shift = key[i]
        decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        decrypted_text += decrypted_char

    return decrypted_text

if __name__ == '__main__':

    # Generowanie szyfru Beale
    key, cipher_text = generate_beale_cipher()
    print("Klucz:", key)
    print("Zaszyfrowany tekst:", cipher_text)

    # Deszyfrowanie szyfru Beale
    decrypted_text = decrypt_beale_cipher(key, cipher_text)
    print("Odszyfrowany tekst:", decrypted_text)

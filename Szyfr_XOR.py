def xor_encrypt_decrypt(text, key):
    encrypted_text = ""
    for i in range(len(text)):
        encrypted_char = chr(ord(text[i]) ^ ord(key[i % len(key)]))
        encrypted_text += encrypted_char
    return encrypted_text

if __name__ == '__main__':

    plain_text = "Hello, World!"
    key = "secret"

    cipher_text = xor_encrypt_decrypt(plain_text, key)
    print("Zaszyfrowany tekst:", cipher_text)

    decrypted_text = xor_encrypt_decrypt(cipher_text, key)
    print("Odszyfrowany tekst:", decrypted_text)

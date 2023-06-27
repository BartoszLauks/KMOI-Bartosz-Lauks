import random


class HomophonicCipher:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.key = {}

        self.generate_key()

    def generate_key(self):
        candidates = [str(i) for i in range(10)]

        for letter in self.alphabet:
            count = random.choice([1, 2])

            count = min(count, len(candidates))

            if count > 0:
                code = random.sample(candidates, count)

                for digit in code:
                    candidates.remove(digit)

                self.key[letter] = "".join(code)

        print("Mapa szyfrująca:")
        for letter, code in self.key.items():
            print(letter, "->", code)

    def encrypt(self, message):
        encrypted_message = ""

        for char in message.upper():
            if char in self.alphabet:
                code = self.key.get(char)
                if code:
                    encrypted_message += code + " "
                else:
                    encrypted_message += char + " "

        return encrypted_message.rstrip()

    def decrypt(self, encrypted_message):
        decrypted_message = ""

        codes = encrypted_message.split()

        for code in codes:
            for letter, c in self.key.items():
                if code == c:
                    decrypted_message += letter

        return decrypted_message

if __name__ == '__main__':

    cipher = HomophonicCipher()

    message = "HELLO WORLD"
    encrypted = cipher.encrypt(message)
    decrypted = cipher.decrypt(encrypted)

    print("Wiadomość: ", message)
    print("Zaszyfrowana wiadomość: ", encrypted)
    print("Odszyfrowana wiadomość: ", message )

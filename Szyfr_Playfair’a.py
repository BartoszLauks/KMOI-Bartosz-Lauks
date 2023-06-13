import string

def prepare_message(message):
    message = message.upper().replace("J", "I")
    message = message.translate(str.maketrans("", "", string.punctuation + string.digits + " "))
    return message

def generate_key_square(key):
    key = key.upper().replace("J", "I")
    key = key.translate(str.maketrans("", "", string.punctuation + string.digits + " "))

    # Tworzenie kwadratu szyfru
    key_square = []
    row = []
    for char in key:
        if char not in row:
            row.append(char)
            if len(row) == 5:
                key_square.append(row)
                row = []

    alphabet = string.ascii_uppercase.replace("J", "")
    for char in alphabet:
        if char not in row:
            row.append(char)
            if len(row) == 5:
                key_square.append(row)
                row = []

    return key_square

def find_char_position(key_square, char):
    for i in range(5):
        for j in range(5):
            if key_square[i][j] == char:
                return i, j
    return None

def encrypt(message, key):
    message = prepare_message(message)
    key_square = generate_key_square(key)

    pairs = []
    i = 0
    while i < len(message):
        if i == len(message) - 1 or message[i] == message[i + 1]:
            pairs.append((message[i], 'X'))
            i += 1
        else:
            pairs.append((message[i], message[i + 1]))
            i += 2

    ciphertext = ""
    for pair in pairs:
        char1 = pair[0]
        char2 = pair[1]

        position1 = find_char_position(key_square, char1)
        position2 = find_char_position(key_square, char2)

        if position1 is not None and position2 is not None:
            row1, col1 = position1
            row2, col2 = position2

            if row1 == row2:
                ciphertext += key_square[row1][(col1 + 1) % 5]
                ciphertext += key_square[row2][(col2 + 1) % 5]
            elif col1 == col2:
                ciphertext += key_square[(row1 + 1) % 5][col1]
                ciphertext += key_square[(row2 + 1) % 5][col2]
            else:
                ciphertext += key_square[row1][col2]
                ciphertext += key_square[row2][col1]
        else:
            ciphertext += char1 + char2

    return ciphertext

def decrypt(ciphertext, key):
    key_square = generate_key_square(key)

    pairs = []
    i = 0
    while i < len(ciphertext):
        pairs.append((ciphertext[i], ciphertext[i + 1]))
        i += 2

    plaintext = ""
    for pair in pairs:
        char1 = pair[0]
        char2 = pair[1]

        position1 = find_char_position(key_square, char1)
        position2 = find_char_position(key_square, char2)

        if position1 is not None and position2 is not None:
            row1, col1 = position1
            row2, col2 = position2

            if row1 == row2:
                plaintext += key_square[row1][(col1 - 1) % 5]
                plaintext += key_square[row2][(col2 - 1) % 5]
            elif col1 == col2:
                plaintext += key_square[(row1 - 1) % 5][col1]
                plaintext += key_square[(row2 - 1) % 5][col2]
            else:
                plaintext += key_square[row1][col2]
                plaintext += key_square[row2][col1]
        else:
            plaintext += char1 + char2

    return plaintext

if __name__ == '__main__':

    message = "Hello World"
    key = "KEYWORD"

    encrypted_message = encrypt(message, key)
    print("Szyfrogram:", encrypted_message)

    decrypted_message = decrypt(encrypted_message, key)
    print("Odszyfrowana wiadomość:", decrypted_message)

def fence_cipher_encrypt(message, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in message:
        fence[rail].append(char)
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    encrypted_message = ''.join([''.join(rail) for rail in fence])
    return encrypted_message


def fence_cipher_decrypt(ciphertext, rails):
    fence = [[''] * len(ciphertext) for _ in range(rails)]
    rail = 0
    direction = 1

    for i in range(len(ciphertext)):
        fence[rail][i] = '*'
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if fence[i][j] == '*':
                fence[i][j] = ciphertext[index]
                index += 1

    rail = 0
    direction = 1
    decrypted_message = ''
    for _ in range(len(ciphertext)):
        decrypted_message += fence[rail][_]
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    return decrypted_message


if __name__ == '__main__':
    plaintext = "HELLO WORLD"
    num_rails = 4

    encrypted = fence_cipher_encrypt(plaintext, num_rails)
    print("Encrypted:", encrypted)

    decrypted = fence_cipher_decrypt(encrypted, num_rails)
    print("Decrypted:", decrypted)

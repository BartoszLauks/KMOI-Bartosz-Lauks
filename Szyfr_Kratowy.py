def route_cipher_encrypt(message, rows, columns):
    message = message.replace(" ", "").upper()
    length = len(message)
    grid_size = rows * columns

    if length < grid_size:
        message += "X" * (grid_size - length)
    elif length % grid_size != 0:
        message += "X" * (grid_size - (length % grid_size))

    encrypted_message = ""
    for i in range(0, len(message), grid_size):
        block = message[i:i + grid_size]
        grid = [[0] * columns for _ in range(rows)]
        count = 0

        for r in range(rows):
            for c in range(columns):
                if count < len(block):
                    grid[r][c] = block[count]
                    count += 1

        for c in range(columns):
            for r in range(rows):
                encrypted_message += grid[r][c]

    return encrypted_message


def route_cipher_decrypt(ciphertext, rows, columns):
    grid_size = rows * columns
    decrypted_message = ""
    for i in range(0, len(ciphertext), grid_size):
        block = ciphertext[i:i + grid_size]
        grid = [[0] * columns for _ in range(rows)]
        count = 0

        for c in range(columns):
            for r in range(rows):
                grid[r][c] = block[count]
                count += 1

        for r in range(rows):
            for c in range(columns):
                decrypted_message += grid[r][c]

    return decrypted_message


if __name__ == '__main__':
    plaintext = "HELLO WORLD"
    num_rows = 3
    num_columns = 4

    encrypted = route_cipher_encrypt(plaintext, num_rows, num_columns)
    print("Encrypted:", encrypted)

    decrypted = route_cipher_decrypt(encrypted, num_rows, num_columns)
    print("Decrypted:", decrypted)

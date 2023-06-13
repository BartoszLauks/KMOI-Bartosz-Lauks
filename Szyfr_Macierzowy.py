import numpy as np


def matrix_cipher_encrypt(message, matrix):
    message = message.upper().replace(" ", "")
    size = len(matrix)
    remainder = len(message) % size

    if remainder != 0:
        message += "X" * (size - remainder)

    encrypted_message = ""
    for i in range(0, len(message), size):
        block = np.array([ord(char) - ord('A') for char in message[i:i + size]])
        encrypted_block = np.matmul(matrix, block) % 26
        encrypted_message += ''.join([chr(char + ord('A')) for char in encrypted_block])

    return encrypted_message


def matrix_cipher_decrypt(ciphertext, matrix):
    size = len(matrix)
    inverse_matrix = np.linalg.inv(matrix)
    determinant = round(np.linalg.det(matrix))
    multiplicative_inverse = None

    for i in range(26):
        if (determinant * i) % 26 == 1:
            multiplicative_inverse = i
            break

    if multiplicative_inverse is None:
        raise ValueError("Matrix is not invertible")

    decrypted_message = ""
    for i in range(0, len(ciphertext), size):
        block = np.array([ord(char) - ord('A') for char in ciphertext[i:i + size]])
        decrypted_block = np.matmul(inverse_matrix, block * multiplicative_inverse) % 26
        decrypted_message += ''.join([chr(char + ord('A')) for char in decrypted_block])

    return decrypted_message


if __name__ == '__main__':
    plaintext = "HELLO WORLD"
    encryption_matrix = np.array([[2, 3], [1, 4]])

    encrypted = matrix_cipher_encrypt(plaintext, encryption_matrix)
    print("Encrypted:", encrypted)

    decrypted = matrix_cipher_decrypt(encrypted, encryption_matrix)
    print("Decrypted:", decrypted)

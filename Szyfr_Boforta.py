def beaufort_cipher(message, key):
    key = key.upper()
    encrypted_message = ""
    for i, char in enumerate(message):
        if char.isalpha():
            key_char = key[i % len(key)]
            key_shift = ord(key_char) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord('Z') - ord(char) + key_shift + 1) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord('z') - ord(char) + key_shift + 1) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message

if __name__ == '__main__':

    # Example usage
    message = "Hello, world!"
    key = "KEY"

    encrypted_message = beaufort_cipher(message, key)
    print("Message : ", message)
    print("Encrypted message:", encrypted_message)

def vigenere_encode(msg, key):
    result = ''
    for i in range(len(msg)):
        char = msg[i]
        key_char = key[i % len(key)]

        new_code = (ord(char) + ord(key_char)) % 256
        result += chr(new_code)

    return result


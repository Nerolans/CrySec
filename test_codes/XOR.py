def XOR_encode(msg, key):
    newS = ""
    count = 0
    for char in msg:
        b_char = ord(char)
        key_char = key[count % len(key)]
        b_key = ord(key_char)

        b_xor = b_char ^ b_key

        newS += chr(b_xor)
        count += 1

    return newS
def shift_encode(msg, key):
    k = int(key)
    result = ""
    for char in msg:

        new_code = (ord(char) + k) % 256
        result += chr(new_code)
    return result

def shift_decode(msg, key):
    k = int(key)
    return encode(msg, -k)
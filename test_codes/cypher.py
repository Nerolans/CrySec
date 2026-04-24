from statistics import mode

def shift_encode(msg, key):
    result = ""
    for char in msg:
        new_code = (ord(char) + key)
        result += chr(new_code)
    return result

def shift_decode(msg, key):
    n_key = -key
    return shift_encode(msg, n_key)

def shift_findKey(msg):
    result = 0
    found = False

    while found is False:
        char = mode(msg)
        tmpKey = abs((ord(char)-ord('e')))
        tmpChar = chr(abs(ord(char)-tmpKey))

        if tmpChar == "e":
            found = True
            result = tmpKey
        else:
            msg = msg.replace(char, '')

    return result
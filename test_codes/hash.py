import hashlib

def clean_secret(corrupted_secret):
    fixed_chars = []
    for char in corrupted_secret:
        if ord(char) > 255:
            try:
                real_char = char.encode('utf-16le').decode('utf-8')
                fixed_chars.append(real_char)
            except:
                fixed_chars.append(char)
        else:
            fixed_chars.append(char)
    return "".join(fixed_chars)

def hash_1(msg):
    msg_encode = msg.encode('utf-8')
    newS = hashlib.sha256(msg_encode)
    print(newS.hexdigest())
    return newS.hexdigest()

def verify(msg, hash):
    if hash_1(msg) == hash:
        return True
    else:
        return False

import hashlib

def hash(msg):
    newS = hashlib.sha256(msg.encode("utf-32"))
    return newS.hexdigest()

def verify(msg, hash):
    if hashlib.sha256(msg) == hash:
        return True
    else:
        return False

import hashlib

def hash(msg):
    newS = hashlib.sha256(msg)
    return newS

def verify(msg, hash):
    if hashlib.sha256(msg) == hash:
        return True
    else:
        return False

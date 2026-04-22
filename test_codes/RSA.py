import math
import secrets
import random
import time


def rsa_encode(msg, n, e):
    result = b""
    for char in msg:
        number = pow(ord(char), e, n)
        result += int.to_bytes(number, length=4)
    return result




################################################################################################
def rsa_decodeSecond(msg, d, n):
    arr = msg.split(" ")
    rslt = ""
    for nbr in arr:
        decoded = pow(int(nbr), d, n)
        rslt += chr(decoded)
    return rslt

def rsa_decodeFirst():
    #put this in the Servers_test part
    keys = generate_keys()
    semiPrime_n = keys[0]
    keyPublic_e = keys[1]
    keyPrivate_d = keys[2]
    return keys

def generate_keys():
    #genretes prime numbers WORKS
    p1 = generate_prime(10, 100)
    p2 = generate_prime(10, 100)
    print("p1:", p1)
    print("p2:", p2)

    #Totient WORKS
    semiPrime_n = p1*p2
    print(semiPrime_n)
    keyPublic_e = 0
    keyPrivate_d = 0

    totient = (p1-1)*(p2-1)

    #select the public key (letter 'e') WORKS
    while True:
        keyPublic_e = generate_prime(100, totient-1)
        if totient % keyPublic_e != 0:
            break

    #select the private key (letter 'd') WORKS
    while True:
        #generates a rdm number
        keyPrivate_d = secrets.randbelow(totient-1)
        #checks if it's a factor of the semiprime (letter n) AND checks if the product of D and E mod T is 1
        if keyPrivate_d != 0 and semiPrime_n % keyPrivate_d != 0 and (keyPrivate_d * keyPublic_e) % totient == 1:
            break

    return semiPrime_n, keyPublic_e, keyPrivate_d

#generates a prime number between a minimum and a maximum
def generate_prime(min, max):
    list_prime = [i for i in range(min, max) if isPrime(i)]
    random_prime = random.choice(list_prime)
    return random_prime

#TEST Primaire
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
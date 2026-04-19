import math
import secrets

def rsa_encode(msg, n, e):
    result = ""
    print(pow(ord('h'), 8484347, 2061654263))
    for char in msg:
        newChr = (pow(ord(char), e, n))
        result += str(newChr) + " "
    result = result[:-1]
    return result

def rsa_decode():
    #generate two prime number

    #put this in the Servers_test part
    keys = generate_keys()
    semiPrime_n = keys[0]
    keyPublic_e = keys[1]
    keyPrivate_d = keys[2]


def generate_keys():
    p1 = generate_prime(1000, 10000)
    p2 = generate_prime(1000, 10000)
    #Totient
    semiPrime_n = p1*p2
    keyPublic_e = 0
    keyPrivate_d = 0
    totient = (p1-1)*(p2-1)
    #select a public key


    #select the public key (letter 'e')
    while True:
        keyPublic_e = secrets.randbelow(totient-1)
        if totient % keyPublic_e is not 0:
            break


    #select the private key (letter 'd')
    while True:
        keyPrivate_d = secrets.randbelow(totient-1)
        if semiPrime_n % keyPrivate_d is not 0 and (keyPrivate_d * keyPublic_e) % totient is 1:
            break

    return semiPrime_n, keyPublic_e, keyPrivate_d

#generates a prime number between a minimum and a maximum
def generate_prime(min, max):
    count = 0
    while True or count < 10000:
        number = secrets.randbelow(max-min)+min
        if isPrime(number):
            return number
        count += 1
    return 0


#TEST Primaire
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%1 == 0:
            return False
        else:
            return True



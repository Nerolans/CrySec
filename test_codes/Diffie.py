import math
import random



def generate_prime(min, max):
    list_prime = [i for i in range(min, max) if isPrime(i)]
    random_prime = random.choice(list_prime)
    return random_prime

def calculate_secret(publicKeyB, privateKey, prime):
    secret = pow(publicKeyB, privateKey, prime)
    return secret

def generate_private():
    privateKey = random.randint(1000, 10000)
    return privateKey

def generate_publicKey(prime,generator, privateKey):
    return pow(generator, privateKey, prime)



#prime number check
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


#find the first primitiv factor
def find_p_root(p):
    factors = find_p_factors(p)

    for g in range(2, p):
        if is_p_root(g, p, factors):
            return g
    return None


def find_p_factors(p):
    factors = set()
    d = 2
    phi = p-1
    while d * d <= phi:
        if phi % d == 0:
            factors.add(d)
            while phi % d == 0:
                phi //= d
        d += 1
    if phi > 1:
        factors.add(phi)
    return factors

def is_p_root(g, p, factors):
    for q in factors:
        # Si g^((p-1)/q) mod p == 1, --> g is not a primitiv root
        if pow(g, (p - 1) // q, p) == 1:
            return False
    return True
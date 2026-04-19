import math
import secrets



def generate_prime(min, max):
    count = 0
    while True or count < 10000:
        number = secrets.randbelow(max-min)+min
        if isPrime(number):
            return number
        count += 1
    return 0

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%1 == 0:
            return False
        else:
            return True
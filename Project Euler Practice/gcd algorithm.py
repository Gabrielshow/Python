#Euclid's algorithm
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

gcd(24, 32)


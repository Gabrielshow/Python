#Cryptomath Module
#Euclid's algorithm
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


#using euclid's extended algorithm to find the modular inverse of a number
def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None # no mod inverse if a & m aren't relatively prime.
     
     #Calculate using the extended Euclidean algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # Note that // is the integer division operator.
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
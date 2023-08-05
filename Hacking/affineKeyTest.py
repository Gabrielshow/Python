#affine key test
#this program proves that the keyspac of the affine cipher is limited
# to less than len(SYMBOLS) ^ 2.

import affinecipher, Cryptomath

message = ' Make things as simple as possible, but not simpler.'
for keyA in range(2, 80):
    key = keyA * len(affinecipher.SYMBOLS) + 1
    
    if Cryptomath.gcd(keyA, len(affinecipher.SYMBOLS)) == 1:
        print(keyA, affinecipher.encryptMessage(key, message))
        
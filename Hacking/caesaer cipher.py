#ceasar cipher
#the string to be encryted/decryted:
message = input('enter message to encrypt/decrypt: ')

#the encryption/decryption key:
key = int(input('enter key for caeser cipher ')) #don't forget to convert this to string

# whether the program encypts or decrypts:
mode = input('type e to encrypt and d to decrypt ') # set to either 'encrypt' or 'decrypt'.

#Every possible symbol that can be encrypted:
SYMBOLS = 'ABDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/'

#Store the encrypted/decrypted form of the message:
translated = ''

for symbol in message:
    #Note: Only symbols in the SYMBOLS string ca be encrypted/decrypted.
    if symbol in SYMBOLS:
        symbolIndex  =  SYMBOLS.find(symbol)
        
        #perform encryption/decryption:
        if mode == 'e':
            translatedIndex = symbolIndex + key
        elif mode == 'd':
            translatedIndex = symbolIndex - key
            
        #Handle wraparound, if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
            
        translated = translated + SYMBOLS[translatedIndex]
    else:
        #append the symbol without encrypting/decrypting:
        translated = translated + symbol
        
#output the translated string:
print(translated)
#Caesar cipher Hacker

message = 'guv6Jz!J6rp5r7Jzr66ntrM'
SYMBOLS ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#loop through every possible key:
for key in range(len(SYMBOLS)):
    #it is important to set translated to the blank string so that the
    #previous iteration's value for translated is cleard:
    translated = ''
    
    #the rest of the program is almost the same as the Caesar program:
    
    # loop through each symbol in message:
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
            
            #handle wraparound:
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
                
            #Append the decrypted symbol:
            translated = translated + SYMBOLS[translatedIndex]
                
        else:
            #Append the symbol without encrypting/decrypting:
            translated = translated + symbol
                
    #Display every possible decrypion:
    print('Key #%s: %s' % (key, translated))
        
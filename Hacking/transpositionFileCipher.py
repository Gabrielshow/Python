#transposition Cipher encrypt/decrypt file

import time, os, sys
import transpositiondecryption, transpositionencryption

def main():
    inputFilename = 'beaver.txt'
    outputFilename = 'beaver.encrypted.txt'
    myKey = 10
    myMode = 'encrypt' # set to encrypt or decrypt
    
    #if the input does not exist, the program terminates early:
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()
        
    #If the output file already exists, give the user a chance to quit:
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()
        
        #Read in the message from the input file:
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()
        
    print('%sing..' % (myMode.title()))
        
    #measure how long the encryption/decryption takes:
    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionencryption.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositiondecryption.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))
        
    #write out the translated message to the output file:
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()
        
    print('Done %sing %s (%s characters). ' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))
        
# if transpositioncipherFile.py is run(instead of imported as a module),
# call the main() function:
if __name__ == '__main__':
    main()
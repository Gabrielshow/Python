#transposition cipher
def main():
    myMessage = input('Enter message to encrypt with transposition cipher. ')
    myKey = int(input('Enter key for the transposition cipher. '))
    
    ciphertext = encryptMessage(myKey, myMessage)
    
    #Print the encrypted string in ciphertext to the screen, with
    # a | ("pipe' character) after it in case there are spaces at
    # the end of the encrypted message:
    print(ciphertext + '|')
    return ciphertext
    
    
def encryptMessage(key, message):
    # each string in ciphertext represents a column in the grid:
    ciphertext = [''] * key
    
    # Loop through each column in ciphertext:
    for column in range(key):
        currentIndex = column
        
        # Keep looping until currenIndex goes past the message length:
        while currentIndex < len(message):
            # place the character at currentindex in message at hte
            # end of the current column in the ciphertext list:
            ciphertext[column] += message[currentIndex]
            
            # move currentIndex over:
            currentIndex += key
    # convert the ciphertext list into a single string value and return it:
    return''.join(ciphertext)

#If transpositionEncrypt.py is run(instead of imported as a module_) call
# the main() function:
if __name__ == '__main__':
    main()
            
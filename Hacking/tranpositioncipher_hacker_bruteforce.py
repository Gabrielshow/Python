import transpositiondecryption

def main():
    myMessage = """ AaKoo soeDe5 b4sn ma reno o ra'lhlrrceey e enlh na indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE"""
    
    hackedMessage = hackTransposition(myMessage)
    
    if hackedMessage == None:
        print('Failed to hack encryption.')
    else:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        

def hackTransposition(message):
    print('Hacking...')
    
    # python prograns can be stopped at any time by pressing
    # Ctrl-C (on Windows) or Ctrl-D (on macOS and Linux):
    print('(Press Ctrl-C (on Windows) or Ctrl-D ( on macOS and Linux) to quit at any time.)')
    
    #Brute-force by looping through every possible key:
    for key in range(1, len(message)):
        print('Trying key #%s..' % (key))
        
        decryptedText = transpositiondecryption.decryptMessage(key, message)
        
        #this won't run because detectEnglish has not be created yet
        # and also detectEnglish has not been imported
        #uncomment this if you have implemented the detectEnglish module
        #if detectEnglish.isEnglish(decryptedText):
            #ask user if this is the correct decryption:
           # print()
            #print('Possible encryption hack:')
            #print('Key %s: %s' % (key, decryptedText[:100]))
            #print()
            #print('Enter D if done, anything else to continue hacking:')
            #response = input('>')
            
            #if response.strip().upper().startswith('D'):
             #   return decryptedText
        
    #return None

if __name__ == '__main__':
    main()

    
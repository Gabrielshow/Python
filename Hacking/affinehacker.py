# Hacking the affine cipher
impoer affinecipher, Cryptomath, detectEnglish

# detectEnglish module has not been implemented yet hence this code will not work

SILENT_MODE = False

def main():
    #some message hack
    myMessage = """5QG9ol3La6QI93!xQxaia6faQL8QdaQG1!!axQARKa!!AuaRKQADQAKQG93!xQx AGaAfaQ1QX3o1RQARL9Qda!AafAruQLX1LQALQI1iQX3o1RN"Q5!RQP36ARu"""
    
    hackedMessage = hackAffine(myMessage)
    
    if hackedMessage != None:
        # The plaintext is displayed on the screen. for tge convenience of
        #the user, we copy the text of the code to the clipboard:
        print('Copying hacked Message to clipboard:')
        print(hackedMessage)
    else:
        print('Failed to hack encryption.')
        
def hackAffien(message):
    print('Hacking...')
    
# Here we're replacing the values index with
# the index of the key.
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
# A becomes L, B becomes F, etc.

import sys, random

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
	myMessage = """
	Words do not express thoughts very well; every thing immediately becomes a little different, a little distorted, a little foolish. 
	And yet it also pleases me and seems right that what is of value and wisdom of one man seems nonsense to another.
	"""
    
    # Order the alphabet specifically as our key.
    # This is our security feature.
    # Amount of combinations = 26*25*24*23...
	myKey = 'RHNUTGMCSLAODYBXVKIWQFEJZP'
    
	myMode = 'encrypt'

	checkValidKey(myKey)

	if myMode == 'encrypt':
		translated = encryptMessage(myKey, myMessage)
	elif myMode == 'decrypt':
		translated = decryptMessage(myKey, myMessage)
	print('Using key: %s' % (myKey))
	print('The %sed message is:' % (myMode))
	print(translated)

def checkValidKey(key):
	# Convert key and characters to list.
	keyList = list(key)
	lettersList = list(SYMBOLS)
    
    # Checks both contain "A...Z".
	keyList.sort()
	lettersList.sort()
	if keyList != lettersList:
		keyList = ''.join(keyList)
		print("Key List:\t\t\t" + keyList)
		lettersList = ''.join(lettersList)
		print("Symbols List:\t\t\t" + lettersList)
		sys.exit('There is an error in the key or character set.')

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = ''
    charsA = SYMBOLS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and SYMBOLS strings are used.
        charsA, charsB = charsB, charsA

    for character in message:
    	# Encrypt: if upper in SYMBOLS(A)
    	# Decrypt: if upper in key(B)
        if character.upper() in charsA:
        
            # Find index of original item
            symIndex = charsA.find(character.upper())
            
            if character.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()  
        else:
            translated += character

    return translated

def getRandomKey():
    key = list(SYMBOLS)
    random.shuffle(key)
    return ''.join(key)

if __name__ == '__main__':
    main()
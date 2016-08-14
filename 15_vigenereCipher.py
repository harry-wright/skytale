# This could easily be turned into a One-Time-Pad (unbreakable) cipher.
# To achieve this you would require:
# 1) The key to be the same length as the message.
#		len(myMessage) == len(myKey)
# 2) The key to be made up of /truly/ random symboles.
# 3) That each key is used once per message.


import random

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
	myMessage = """
	Fzv bqnzczpmre kkj hcispl kku af elinjqcl ka cvxs pivd nwzgj ymliizvepou ip fzv mussl.
	Zr qfn wbp pk, kgl plvc iv xgexoi fmkqf, rgg cftvfadxv pipxtlvghn.
	Sbk zg gklmv pj fgf alqy af bsp yrb kov bjzolvvnv ax fpqsen pamilhvw.
	"""
	myMode = 'decrypt' # set to 'encrypt' or 'decrypt'
	myKey = "mSrTDkRhR"

	if myMode == 'encrypt':
		translated = encryptMessage(myKey, myMessage)
		
	elif myMode == 'decrypt':
		translated = decryptMessage(myKey, myMessage)

	print('%sed message:' % (myMode.title()))
	print(translated)


def encryptMessage(key, message):
	return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
	return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):

	# Stores the encrypted/decrypted message string.
	translated = [] 

	keyIndex = 0
	key = key.upper()

	for character in message:
	
		# Find index of character.
		num = SYMBOLS.find(character.upper())
		
		# If number was found.
		if num != -1:
			if mode == 'encrypt':
			
				# Index + Key[0].
				num += SYMBOLS.find(key[keyIndex])
				
			elif mode == 'decrypt':
				num -= SYMBOLS.find(key[keyIndex])
				
			# Wrap around, so mod(symbols).
			num %= len(SYMBOLS)

			# Keep case of character.
			if character.isupper():
				translated.append(SYMBOLS[num])
			elif character.islower():
				translated.append(SYMBOLS[num].lower())

			# Move to next key letter.
			keyIndex += 1
			if keyIndex == len(key):
				keyIndex = 0
		else:
			# The symbol was not in SYMBOLS.
			translated.append(character)

	return ''.join(translated)

if __name__ == '__main__':
	main()
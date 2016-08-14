# To properly grasp the concept within, an understanding
# of modular arithmetic is required. The learning curve, for me at least,
# started getting pretty steep here. 
# Modular mathematics appear to be used heavily throughout Cryptography, 
# so learning how the script below operates is far from being classed as wasted time.
#
# Summarising the encryption/decryption process:
#
# Encrypt d as e ≅ (da+b) % N
# encrypted = ( symIndex * keyA + keyB ) % len(SYMBOLS)
#
# Well how does this work?
# Because the encrypted value is congruent to the decrypted value in mod(x),
# the length of the symbols, we can easily reverse this by solving for d.
#
# e = d * a + b 			# 67 			| 1705 + 72 = 1777 	% 95 = 67
# e - b = d * a 			#  67 - 72 = -5	| 55 * 31 = 1705	% 95 = 90 ~ so are congruent as 95
# (e - b)/a = (d * a)/a		# -5/a			| 1705/a
# (e - b)/a = d				# -5/a			| 55
# here because we've moved to top it becomes opposite
# a[-1](e - b) = d			#46 * -5 = -230 % 95 = 55|				| 55
#
# We're looking for 31[-1]
#(I*N)+1   /  A
#
#(15*95)+1  / 31 = 46   ± any whole number, int,  will be multiplicative inverse
#
#
# It's worth nothing: a[-1] != 1/7. It is actually 7[-1] mod (x).
# This is where Euclid's algorithm comes into play.
#
# Decrypt e as d ≅ m(e-b) % N 
# decrypted = modInverseOfKeyA * ( symIndex - keyB ) % len(SYMBOLS)

import sys, cryptomath, random

# Space is included. Length is 95.
SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def main():

	# e = print (SYMBOLS[67]) = c
	# d = print (SYMBOLS[55])  = W
	myMessage = """
	What matters most is how well you walk through the fire.
	"""
    
	myKey = 3017
	myMode = 'encrypt'

	if myMode == 'encrypt':
		translated = encryptMessage(myKey, myMessage)
		
	elif myMode == 'decrypt':
		translated = decryptMessage(myKey, myMessage)
    
	print('Key: %s' % (myKey))
	print('%sed text:' % (myMode.title()))
	print(translated + "\n")

def getKeyParts(key):

	# number = quotient * mod + remainder
	# key = ( keyA * len(SYMBOLS) ) + keyB
	
    keyA = key // len(SYMBOLS) # 31 full rotations (31 * 95 = 2945)
    keyB = key % len(SYMBOLS)  # 72 remainder (2945 + 72 = 3017)
    
    return (keyA, keyB)

def checkKeys(keyA, keyB, mode):

	print ("Key A: " + str(keyA) + "\nKey B: " + str(keyB))
	if keyA == 1 and mode == 'encrypt':
		sys.exit('The affine cipher becomes incredibly weak when key A is set to 1. Choose a different key.')
	if keyB == 0 and mode == 'encrypt':
		sys.exit('The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
	if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
		sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
	# Relatively prime means that the greatest factor between 2 numbers is 1.
	if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
		sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(SYMBOLS)))

def encryptMessage(key, message):

	keyA, keyB = getKeyParts(key)
	checkKeys(keyA, keyB, 'encrypt')
	ciphertext = ''
    
	for symbol in message:
		if symbol in SYMBOLS:
			symIndex = SYMBOLS.find(symbol)
			
			ciphertext += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
            
		else:
			ciphertext += symbol
	return ciphertext

def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    
    plaintext = ''

    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
             
            plaintext += SYMBOLS[modInverseOfKeyA * ( symIndex - keyB ) % len(SYMBOLS)]
            
        else:
            plaintext += symbol
    return plaintext

def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB

if __name__ == '__main__':
    main()
# Import relevant modules and our other previous scripts.

import random, sys, transpositionEncrypt, transpositionDecrypt

def main():
	
	# The number given to seed is an arbitrary starting point.
	# The seed function performs calculations on this number.
	
	random.seed(43) 

	# We are going to run 20 tests.
	
	for i in range(20):

		# The message we're going to use is a string of the alphabet.
		# We will generate a random amount, e.g. A...ZA...ZA...Z .
		
		message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
		
		# Shuffle the letters so at first turn it into a list.
		
		message = list(message)
		
		# Then shuffle the list and return it to a string.
		
		random.shuffle(message)
		message = ''.join(message)

		# Show what number test is ongoing and the first
		# 50 characters of the message.
		
		print('Test #%s: "%s..."' % (i+1, message[:50]))

		# Loop for each character of the message.
		# Start with index 1 as we cannot have a key of zero.
		
		for key in range(1, len(message)):

			# Encrypt scrambled string.
			
			encrypted = transpositionEncrypt.encryptMessage(key, message)
			
			# Decrypts encrypted string.

			decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

			# Check if message = decrypted.
			
			if message != decrypted:

				print('Mismatch with key %s and message %s.' % (key, message))

				print(decrypted)

				sys.exit()

	print('Transposition cipher test passed.')

if __name__ == '__main__':
	main()
message = 'GUVF VF ZL FRPERG ZRFFNTR.'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# So here the length, len(LETTERS) = 26
# And range(len(LETTERS)) = (0,26)
# They key is: key = 0, 1, 2, 3, ... 25

for key in range(len(LETTERS)):

		# Set translated to null after each loop
		
		translated = ''
		
		for symbol in message:
			if symbol in LETTERS:
				num = LETTERS.find(symbol)

				num = num - key

				if num < 0:
					num = num + len(LETTERS)

				# Add each letter to to the value of translated.
				
				translated = translated + LETTERS[num]

			else:
			
				# Add the symbol without encrypting/decrypting
				
				translated = translated + symbol

		print('Key #%s: %s' % (key, translated))
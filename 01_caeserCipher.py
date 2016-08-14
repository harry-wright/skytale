
# Specifically import the 'argv' function from the 'sys' module.
# This function opens the script with an argument we define.
# In this case it is 'usermode' we will define.
# The first value of 'script' can be ignored, but must always be added.
# To use 'argv' add the arguments within the terminal.

from sys import argv
(script, usermode) = argv

# Give the variable 'mode' the value of 'usermode'.
# The modes we will be able to give are either 'encrypt' or 'decrypt'.
# Example: "Harry$> python3.5 caesarEncrypt.py encrypt" 

mode = usermode

message = input('Message to be encrypted:')

# This is our encryption key. We will move each letter 13 places along the alphabet.
# In this case, the letter 'A' would become 'N'.

key = 13

# This is the string we will use to step our values up and down.

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ''

# Transforms the text to uppercase.

message = message.upper()

# Starts a loop that will run for each letter of the message.

for symbol in message:

	# Checking for special characters.

	if symbol in LETTERS:

		# Find the numerical value of the symbol.

		num = LETTERS.find(symbol)

		# If encrypting, add the value. Vice versa for decrypting.

		if mode == 'encrypt':
			print(num)
			num = num + key

		elif mode == 'decrypt':
			num = num - key

		# So what happens when we need to go beyond the letter 'Z'?

		if num >= len(LETTERS):

			print(num)
			# Say we are using the letter Z.
			# So Z = 26, but as lists always start with 0, Z = 25.
			# So 25 + 13 = 38. Subtract the length of the alphabet.
			# 38 - 26 (the length) = 12. Gives the value we need.

			num = num - len(LETTERS)
			print(num)
			
		elif num < 0:

			# If below 0, add the length of the alphabet.
			# Opposite of above.

			num = num + len(LETTERS)

		# Add each encrypted letter to the 'translated' value.

		translated = translated + LETTERS[num]

	else:

		# Return special values without encryption.

		translated = translated + symbol

print(translated)
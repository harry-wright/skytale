# We will requires some math functions for decryption.

import math

def main():
	
	# Here the length, len = 30.
	
	message = "Cenoonommstmme oo snnio. s s c"
	
	key = 8
	
	# Pass values to function decryptMessage.
	
	output = decryptMessage(key, message)
	
	print("<decrypted>" + output + "<decrypted>")
	
def decryptMessage(key, message):

	# Round up 30/8, which equals 4.
	# This is how many columns we require to decrypt the message.
	
	numcols = math.ceil( len(message) / key )
	
	# We encrypted the message with the
	# the amount of rows as the key.
	
	numrows = key
	
	# Each item represents a column in the grid.
	
	result = [""] * numcols
	print(numcols)
	
	# As we didn't use every single row and column when encrypting
	# we need to acknowledge this. Failure to do so would result
	# in the end of our message being corrupted.
	# So 'voidvals' represent the unused grid spaces.
	
	voidvals  = ( numcols * numrows ) - len(message)
	
	# Define our starting points.
	
	col = 0
	row = 0
	
	# Loop for each character in the encrypted message.
	
	for symbol in message:
	
		# First loop would return result[0] += "C"
		# Which would e ["C","","",""].
	
		result[col] += symbol

		# We then move our point to the next column.
		# Which would in turn be the 'e': ["C","e","",""].
		
		col += 1
	
		# So first, we only have 4 columns. If we reach or pass
		# that value we need to go back to the first column.
		# OR this must be done when we reach an unused grid space.
		# So ( IF COL = 3 ) & ( ROW >= 8 - 2 ).
		
		if (col >= numcols) or ( col == numcols - 1 and row >= key - voidvals ):
		
			col = 0
			row +=1
			
	# Join the end result and return the value
	
	final = ''.join(result)
	return (final)
	
if __name__ == '__main__':
	main()
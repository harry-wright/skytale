# Example usage:
# Harry$> python3.5 transpositionFiles.py encrypt document.txt encrypteddoc.txt 13

# We will time the process, open files, use system exit 
# and our earlier modules.

import time, os, sys, transpositionEncrypt, transpositionDecrypt

from sys import argv
(script, usermode, inputfile, outputfile, userkey) = argv

def main():

	# Parameters specified in 'argv'.

	inputFilename = inputfile
	outputFilename = outputfile
	myKey = int(userkey)
	myMode = usermode
    
    
	# Check that the input files exists.

	if not os.path.exists(inputFilename):
		print('The file %s does not exist. Quitting...' % (inputFilename))
		sys.exit()


	# If a file with the name of output file exists,
	# check if the user wishes to overwrite.

	if os.path.exists(outputFilename):
		print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
		response = input('> ')
		if not response.lower().startswith('c'):
			sys.exit()


    # Read in the message from the input file.
    # Open -> Read & Assign -> Close.

	fileObj = open(inputFilename)
	content = fileObj.read()
	fileObj.close()
	print('%sing...' % (myMode.title()))


	# Measure how long the encryption/decryption takes.

	startTime = time.time()
    
	if myMode == 'encrypt':
		translated = transpositionEncrypt.encryptMessage(myKey, content)

	elif myMode == 'decrypt':
		translated = transpositionDecrypt.decryptMessage(myKey, content)

	totalTime = round(time.time() - startTime, 2)
	print('%sion time: %s seconds' % (myMode.title(), totalTime))


	# Write out the translated message to the output file.
	# Open & Assign -> Write -> Close.

	outputFileObj = open(outputFilename, 'w')
	outputFileObj.write(translated)
	outputFileObj.close()
	print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
	print('%sed file is %s.' % (myMode.title(), outputFilename))


if __name__ == '__main__':

     main()
import os, re, copy, substitutionCipher, makeWordPatterns

if not os.path.exists('wordPatterns.py'):
	makeWordPatterns.main() # create the wordPatterns.py file
import wordPatterns

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLettersOrSpacePattern = re.compile('[^A-Z\s]')

def main():
	message = """
	Ebkui ub ybw tjxktii wcbqmcwi ftkz etoo; tftkz wcsym sddtusrwtoz htnbdti r oswwot usggtktyw, r oswwot usiwbkwtu, r oswwot gbbosic.
	Ryu ztw sw roib xotriti dt ryu ittdi ksmcw wcrw ecrw si bg froqt ryu esiubd bg byt dry ittdi ybyityit wb rybwctk.
	"""
	
	print('Attempting to solve...\n\n')
	globalMap = hackSimpleSub(message)
	
	for symbol in SYMBOLS:
		print("Candidates for " + symbol + ":")
		print(globalMap[symbol])
		print("\n")
	
	print("Encrypted Message: ")
	print(message)
	
	finalMessage = decryptWithGlobalMap(message, globalMap)
	
	print("Decrypted Message: ")
	print(finalMessage)

def emptyCipherMap():
	return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [],
			'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 
			'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 
			'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []
			}

# Remember this is done for each WORD candidate.
def addLettersToMap(wordMap, cipherword, candidate):

	# Copies with a new instance.
	wordMap = copy.deepcopy(wordMap)

	# For each letter of encrypted.
	for i in range(len(cipherword)):
	
		# If LETTER candidate not yet added to wordMap.
		if candidate[i] not in wordMap[cipherword[i]]:
		
			# Append LETTER to wordMap.
			wordMap[cipherword[i]].append(candidate[i])
			
	return wordMap

def intersectMap(globalMap, wordMap):
# Starting on the first word loop, globalMap has no value so all reach point A.
# On the second word, we loop the alphabet again. For example we haven't used
# 'X', so the loop for this letter goes to point A. Letters that we have values
# for but are not in this word, go to B.
# But then we have 'Q'. This letter's been used before AND is in this word.
# So we only accept the letters that are in BOTH lists.
	
	# Within this function we start a new map.
	functionMap = emptyCipherMap()
	
	# Loop through alphabet.
	for symbol in SYMBOLS:

		# If globalMap[a] does not have a value.
		# On the first loop this will be used for A-Z.
		if globalMap[symbol] == []:
		
			# **** POINT A ****
			
			# Just copy wordMap[a].
			functionMap[symbol] = copy.deepcopy(wordMap[symbol])
			
		# If wordMap[a] does not have a value.
		elif wordMap[symbol] == []:
		
			# **** POINT B ****
			
			# Just copy globalMap[a].
			functionMap[symbol] = copy.deepcopy(globalMap[symbol])
			
		else:
		
			# **** POINT C ****
		
			# For EACH CANDIDATE in globalMap[a].
			# E.g. x,y,z in globalMap{a:x,y,z}.
			for candidateLetter in globalMap[symbol]:
			
				# If that candidate is in our word map.
				# If 'x' in wordMap[a].
				if candidateLetter in wordMap[symbol]:
				
					# Append 'x' to functionMap[a].
					functionMap[symbol].append(candidateLetter)

	return functionMap

def removeSolved(globalMap):

	globalMap = copy.deepcopy(globalMap)
	loopAgain = True
	
	while loopAgain:
	
		# Assume that we will not loop again.
		loopAgain = False

		# Only one possible mapping; add to solved.
		solvedLetters = []
		for cipherletter in SYMBOLS:
			if len(globalMap[cipherletter]) == 1:
				solvedLetters.append(globalMap[cipherletter][0])

		# For each letter of the alphabet.
		for symbol in SYMBOLS:

			# Loops through each solved letter [x,y,z].
			for solved in solvedLetters:
			
				# If a letter is solved, we can remove it from this alphabet letter.
				if len(globalMap[symbol]) != 1 and solved in globalMap[symbol]:
				
					# Remove from list.
					globalMap[symbol].remove(solved)
					
					# If there is only 1 letter left after solving.
					if len(globalMap[symbol]) == 1:
					
						# Letter is now solved, so loop again.
						loopAgain = True
						
	return globalMap

def hackSimpleSub(message):
	# This will be the 'big' map all results are added to.
	globalMap = emptyCipherMap()
	
	# Our message, as a list, in upper case.
	cipherwordList = nonLettersOrSpacePattern.sub('', message.upper()).split()

	# For each word in our message.
	for cipherword in cipherwordList:
	
		# New map for each word.
		wordMap = emptyCipherMap()

		# Get word pattern.
		wordPattern = makeWordPatterns.getWordPattern(cipherword)

		# If pattern isn't found go to next iteration.
		if wordPattern not in wordPatterns.allPatterns:
			continue

		# For each possible word that matched our pattern.
		for candidate in wordPatterns.allPatterns[wordPattern]:
		
			# So wordMap becomes the dictionary with the candidates.
			wordMap = addLettersToMap(wordMap, cipherword, candidate)

		# All letter candidates for the word have been completed and added to wordMap.
		# Now intersect with the globalMap.
		globalMap = intersectMap(globalMap, wordMap)

	# Remove any solved letters from the other lists.
	return removeSolved(globalMap)

def decryptWithGlobalMap(message, globalMap):
	
	key = ['x'] * len(SYMBOLS)
	for symbol in SYMBOLS:
		if len(globalMap[symbol]) == 1:
		
			# Add to key if solved.
			keyIndex = SYMBOLS.find(globalMap[symbol][0])
			key[keyIndex] = symbol
			
		else:
		
			# If we haven't solved the letter modify message with underscores.
			message = message.replace(symbol.lower(), '_')
			message = message.replace(symbol.upper(), '_')
	key = ''.join(key)

	# We've imported out substitutionCipher module.
	# Let's decrypt the message with our partial key and modified message.
	return substitutionCipher.decryptMessage(key, message)

if __name__ == '__main__':
	main()
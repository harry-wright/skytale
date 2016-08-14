UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# A..Z + a..z + [tab]+ [newline]
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'



def loadDictionary():

	# Open -> Read -> Get Dict -> Close.
	dictionaryFile = open('dictionary.txt')

	englishWords = {}

	for word in dictionaryFile.read().split('\n'):

		# 'AARDVARK': None.
		englishWords[word] = None

	dictionaryFile.close()

	# This function return the full dictionary.
	return englishWords



# English dictionary as dict.
ENGLISH_WORDS = loadDictionary()



def getEnglishCount(message):

	message = message.upper()

	message = removeNonLetters(message)

	# Splits string into smaller strings.
	possibleWords = message.split()

	if possibleWords == []:

		return 0.0 # no words at all, so return 0.0

	matches = 0

	for word in possibleWords:

		if word in ENGLISH_WORDS:

			matches += 1

	# 10 matches / 10 words = 1.0 = 100%.
	return float(matches) / len(possibleWords)



# Does what it says it does.
def removeNonLetters(message):

	lettersOnly = []

	for symbol in message:

		if symbol in LETTERS_AND_SPACE:

			lettersOnly.append(symbol)

	return ''.join(lettersOnly)



# Returns True if the string passed is English text.
# (-,x,-), percentage of words that must be english.
# (-,-,x), percentage of content that must be letters or spaces.
def isEnglish(message, wordPercentage=20, letterPercentage=85):

	# Turns decimal of getEnglishCount into percentage.
	wordsMatch = getEnglishCount(message) * 100 >= wordPercentage

	# Remove letters of message and return length.
	numLetters = len(removeNonLetters(message))

	messageLettersPercentage = float(numLetters) / len(message) * 100

	# Does it meet requirements; arguments passed or the default.
	lettersMatch = messageLettersPercentage >= letterPercentage

	# To return true both must be satisfied.
	return wordsMatch and lettersMatch
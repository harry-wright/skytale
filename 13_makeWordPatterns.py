import pprint

# Function returns a string pattern.
#  '0.0.1.2.3': ['AARON', 'LLOYD', 'OOZED'],
def getWordPattern(word):
    word = word.upper()
    nextNum = 0
    
    # Dictionary of letter with corresponding value.
    # e.g. {'A':'1', 'L':'2'}
    letterNums = {}
    
    wordPattern = []

    for letter in word:
    
    	# If letter not yet used.
        if letter not in letterNums:
        	# Add letter with value to dict.
            letterNums[letter] = str(nextNum)
            nextNum += 1
            
        # Example: ['0', '1', '2', '3', '4', '1', '2']
        wordPattern.append(letterNums[letter])
        
    return '.'.join(wordPattern)


def main():
	# Dict of all patterns.
    allPatterns = {}

    fo = open('dictionary.txt')
    wordList = fo.read().split('\n')
    fo.close()

    for word in wordList:
        # Get the pattern for each string in wordList.
        pattern = getWordPattern(word)

        if pattern not in allPatterns:
            allPatterns[pattern] = [word]
        else:
            allPatterns[pattern].append(word)

    fo = open('wordPatterns.py', 'w')
    fo.write('allPatterns = ')
    fo.write(pprint.pformat(allPatterns))
    fo.close()


if __name__ == '__main__':
    main()
import detectEnglish, transpositionDecrypt

def main():
	myMessage = """Bcyglyltheiuodtwdhahtf’nhov pa ea dbtrite e ch meihsufrsydede ;o e ufdm he.eh  f  i rndliyi nleof caoifavpdtg ihelssa ouiwyrnyeteei  a  d ro croypmagg ty:Ibniegees,lselm eietdloree uoile   slnflmh   sn lamewsaoiteftaer letrideo  egnnr,nl les  tng   .rt rtroti oam,sa psob(tisaltinio fvh  hn  ci  analuTs  tca coi,lsodhdnoio   lchedstnfne ottre rnhcesouldtns ienti mnaciid ylrohmweetieyl f fueeofsrBmIoee   ya daa uhiliooea, wraoh htnrohnieonansie isdaeir,in,alai– e rr   uy ni oan,te nntretfstt l a erw aaheenogn,b t  nabnealetf ts l-ns t osawget hgvnfno uvindhe  , h p b c lernre)fessj oiewdg"""

	hackedMessage = hackTransposition(myMessage)

	if hackedMessage == None:
		print('Failed to hack encryption.')
	else:
		print('Copying hacked message to clipboard:')
		print(hackedMessage)



def hackTransposition(message):
	print('Hacking...')


    # Brute-force by looping through every possible key.
    # As before, cannot have a key of zero.
	for key in range(1, len(message)):
		print('Trying key #%s...' % (key))

		decryptedText = transpositionDecrypt.decryptMessage(key, message)

		if detectEnglish.isEnglish(decryptedText):
        	# Check with user to see if the decrypted key has been found.
			print('Possible encryption hack:')
			print('Key %s: %s' % (key, decryptedText[:100]))
			print('Enter D for done, or just press Enter to continue hacking:')
			response = input('> ')

			if response.strip().upper().startswith('D'):
				return decryptedText

	return None

if __name__ == '__main__':
    main()

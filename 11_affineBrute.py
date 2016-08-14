import affineCipher, detectEnglish, cryptomath

SILENT_MODE = False

def main():

    myMessage = """
	m:Q:$ph0Sh08:h[Q|,lhS4:p?he8:htWpYW0p?he8:hQ:<:Up?he8:h0QSO<U:t|6:Qp?h
	e8:hQSO4zhr:xphW4h08:hp2O|Q:h8SU:p?he8:hS4:ph.8Shp::h08W4xphzWYY:Q:40Ul?h
	e8:l$Q:h4S0hYS4zhSYhQOU:p?hR4zh08:lh8|n:h4ShQ:pr:[0hYSQh08:hp0|0Oph2OS?h
	BSOh[|4h2OS0:h08:t`hzWp|xQ::h.W08h08:t`hxUSQWYlhSQhnWUWYlh08:t?h
	R<SO0h08:hS4Ulh08W4xhlSOh[|4$0hzShWphWx4SQ:h08:t?hq:[|Op:h08:lh[8|4x:h08W4xp?h
	e8:lhrOp8h08:h8Ot|4hQ|[:hYSQ.|Qz?hR4zh.8WU:hpSt:ht|lhp::h08:th|ph08:h[Q|,lhS4:p`h.:hp::hx:4WOp?h
	q:[|Op:h08:hr:SrU:h.8Sh|Q:h[Q|,lh:4SOx8h0Sh08W46h08:lh[|4h[8|4x:h08:h.SQUz`h|Q:h08:hS4:ph.8ShzS?
	"""
	
    hackedMessage = hackAffine(myMessage)

    if hackedMessage != None:
        print(hackedMessage)
    else:
        print('Failed to hack encryption.')


def hackAffine(message):
    print('Hacking...')
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    # brute-force by looping through every possible key
    for key in range(len(affineCipher.SYMBOLS) ** 2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue

        decryptedText = affineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print('Tried Key %s... (%s)' % (key, decryptedText[:40]))

        if detectEnglish.isEnglish(decryptedText):
            # Check with the user if the decrypted key has been found.
            print()
            print('Possible encryption hack:')
            print('Key: %s' % (key))
            print('Decrypted message: ' + decryptedText[:200])
            print()
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText
    return None

if __name__ == '__main__':
    main()
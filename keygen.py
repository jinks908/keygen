#!/usr/bin/python

#Password generator

import string
import random
import time

def genPasswd():

	print('''

		..:: Python Random Key Generator ::..

	Which type of passkey would you like to generate?

	1) Letters 				
	2) Numbers
	3) Special Characters
	4) Letters & Numbers
	5) Letters, Numbers, & Special Characters

	'''	)

	passType = int(input())
	passLen = int(input('\n\nHow many characters would you like your password to contain? '))

	pLet = ''.join(random.choice(string.ascii_letters) for _ in range(passLen))
	pNum = ''.join(random.choice(string.digits) for _ in range(passLen))
	pSpec = ''.join(random.choice(string.punctuation) for _ in range(passLen))
	pLetNum = ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(passLen))
	pAll = ''.join(random.choice(string.ascii_letters+string.digits+string.punctuation) for _ in range(passLen))

	while True:
		if passType == 1:
			print('\n\n'+str(pLet))
		elif passType == 2:
			print('\n\n'+str(pNum))
		elif passType == 3:
			print('\n\n'+str(pSpec))
		elif passType == 4:
			print('\n\n'+str(pLetNum))
		elif passType == 5:
			print('\n\n'+str(pAll))
		else:
			print('\n\nSorry, '+str(passType)+' is not a valid passkey option.')
			time.sleep(2)
			genPasswd()
		break


if __name__ == '__main__':
	genPasswd()
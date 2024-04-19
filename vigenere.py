import string
import sys
import os
import argparse


"""
def vigenere_encipher(p,k):
	# given a string p of all lowercase letters, 
	# and a key k of all lowercase letters,
	# return a string of all uppercase letters,
	# which is the vigenere encryption of p by key k.
	
	c = ""
	i = 0
	for pi in p:
		
		# some sample code that only
		# changes the number to uppercase

		
		
		pn = ord(pi)-ord('a')
		cn = pn + ord('A')
		c += chr(cn)

		
		#Knowing 'A' = 65
		#Just need to subtract 64 from each key char,
		# then add that much to the plaintext.	
		

		pass
	return c ;
"""

def vigenere_encipher(p,k):

	#Enciphers a string p based on a key k. Iterates through each letter in p, and cycles through k, capitalizing both.

	#Lowercase to capital is -32
	c = ""
	i = 0
	for letter_pos in range(0, len(p)):
		
		new_plain = chr(ord(p[letter_pos])-32)
		
		if i == len(k):
			i = 0
		new_key = ord(k[i])-32

		#Creates a shift based on the key and applies it to the plaintext,creating our tentative cipher char
		shift = new_key - 65
		ciphered_char = ord(new_plain) + shift

		#Correction for overshooting the available alphabet; will reset back to 'A' + the overshoot
		if ciphered_char > 90:
			overshot_by = ciphered_char - 90
			ciphered_char = overshot_by+64
		c+= chr(ciphered_char)
		i+=1
	return c




def vigenere_decipher(c,k):
	# given a string c of all uppercase letters, 
	# and a key k of all lowercase letters,
	# return a string of all lowercase letters,
	# which is the vigenere decryption of c by key k.

	p = ""
	i = 0
	for letter_pos in range(0, len(c)):
		#Very similar structure as the encryption, only reversed; shift will be subtracted, and overshooting will be handled in the opposite direction.
		if i == len(k):
			i=0
		new_key = ord(k[i])

		shift = new_key - 97
		deciphered_char = ord(c[letter_pos]) - shift

		if deciphered_char < 65:
			overshot_by = 64 - deciphered_char
			deciphered_char = 90-overshot_by

		deciphered_char +=32
		
		p+= chr(deciphered_char)
		i+=1
	return p 


def parse_args():
	parser = argparse.ArgumentParser(description="Encrypt/decrypt stdin by a vigenere cipher. Ignores any character other than alphabetic.")
	parser.add_argument("key", help="encipherment key")
	parser.add_argument("-d", "--decrypt", action="store_true", help="decrypt, instead of encrypting")
	parser.add_argument("-g", "--word_group", type=int, default=5, help="characters per word group")
	parser.add_argument("-G", "--line_group", type=int, default=5, help="word groups per line")
	parser.add_argument("-v", "--verbose", action="store_true", help="verbose")
	return parser.parse_args()

def main(argv):

	args_g = parse_args()

	## gather plain text and format
	t_in = ""
	for line in sys.stdin:
		for c in line:
			if c.isalpha():
				if not args_g.decrypt:
					c = c.lower()
				else:
					c = c.upper()
				t_in += c

	## encrypt/decrypt
	if args_g.decrypt:
		t_out = vigenere_decipher(t_in,args_g.key)
	else:
		t_out = vigenere_encipher(t_in,args_g.key)

	## pretty print ct
	i = 0
	s = ""
	r = args_g.word_group * args_g.line_group

	for c in t_out:
		s += c
		i += 1
		if i%args_g.word_group==0:
			s += ' '
		if i%r==0:
			s += '\n'
	print (s)
	

main(sys.argv)
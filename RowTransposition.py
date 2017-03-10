from CipherInterface import *
import math

class RowTransposition(CipherInterface):
	def __init__(self):
		CipherInterface.__init__(self)
		
	def setKey(self, key):
		self.key = key
		
	def encrypt(self, plain_text):
		cipher_text = ""
		offset = len(self.key)
		plain_text_length = len(plain_text)
		num_rows = math.ceil(plain_text_length/len(self.key))
		enc_dict = {}

		for index, char in enumerate(self.key):
			enc_dict[int(char)] = ""
			enc_dict[int(char)] += plain_text[index::offset]
			if len(enc_dict[int(char)]) != num_rows:
				enc_dict[int(char)] += 'x'

		for char in self.key:
			cipher_text += enc_dict[int(self.key[int(char) - 1])]
							
		return cipher_text
	
	def decrypt(self, cipher_text):
		plain_text = ""
		cipher_length = len(cipher_text)
		num_rows = math.ceil(cipher_length/len(self.key))
		dec_dict = {}
		for char in self.key:
			dec_dict[int(char)] = ""
			dec_dict[int(char)] += cipher_text[0:num_rows]
			cipher_text = cipher_text[num_rows:cipher_length]

		empty = False
		while plain_text != cipher_length:
			for key in dec_dict.keys():
				if not dec_dict[key]:
					empty = True
					break
				plain_text += dec_dict[key][0]
				dec_dict[key] = dec_dict[key][1:len(dec_dict[key])]
			if empty:
				break

		return plain_text
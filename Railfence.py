from CipherInterface import *

class Railfence(CipherInterface):
	def __init__(self):
		CipherInterface.__init__(self)
		
	def setKey(self, key):
		self.key = int(key)
		
	def encrypt(self, plain_text):
		cipher_text = ""
		for row in range(0, self.key):
			cipher_text += plain_text[row::self.key]
								
		return cipher_text
	
	def decrypt(self, cipher_text):
		plain_text = ""
		#length of the cipher text
		cipher_length = len(cipher_text)
		#rows that will need extra letters
		need_extra = range(0, cipher_length % self.key)
		#Dictionary with rows as keys and empty lists as the values
		my_dict = { key:[] for key in range(0, self.key) }
		#amount of letters to iterate through
		jump = (len(cipher_text) // self.key)

		for row in range(0, self.key):
			#if row is one of the rows that needs an extra, jump a little further
			if(row in need_extra):
				for i in range(0, jump+1):
					my_dict[row].append(cipher_text[0])
					cipher_text = cipher_text[1:cipher_length]			
			else:
				for x in range(0, jump):
					if(cipher_text != ''):
						my_dict[row].append(cipher_text[0])
						cipher_text = cipher_text[1:cipher_length]

		empty = False
		while plain_text != cipher_length:
			for key in range(0, self.key):
				if not my_dict[key]:
					empty = True
					break
				plain_text += my_dict[key].pop(0)
			if empty:
				break

		return plain_text
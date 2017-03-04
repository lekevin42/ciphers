from CipherInterface import *

class Vigenere(CipherInterface):
	def __init__(self):
		CipherInterface.__init__(self)
		self.alphabet = self.create_alphabet()
		
	def setKey(self, key):
		self.key = key
		
	def encrypt(self, plain_text):
		cipher_text = ""
		counter = 0
		key_size = len(str(self.key))
		
		for char in plain_text:
			plain_index = self.alphabet.index(char)
			key_index = self.alphabet.index(self.key[counter])
			
			cipher_value = (plain_index + key_index) % 26
			cipher_text += self.alphabet[cipher_value]
			counter += 1
			
			if counter == key_size:
				counter = 0
		
		return cipher_text
		
	def decrypt(self, cipher_text):
		plain_text = ""
		counter = 0
		key_size = len(str(self.key))
		
		for char in cipher_text:
			cipher_index = self.alphabet.index(char)
			key_index = self.alphabet.index(self.key[counter])
			
			plain_value = (cipher_index - key_index) % 26
			plain_text += self.alphabet[plain_value]
			
			counter += 1
			
			if counter == key_size:
				counter = 0
				

		return plain_text
		
	def create_alphabet(self):
		alphabet_list = []
		
		for ascii_val in range(97, 123):
			alphabet_list.append(chr(ascii_val))
		
		
		return alphabet_list
		
def main():
	plain_text = "same"
	key = "bar"
	v = Vigenere()
	v.setKey(key)
	cipher_text = v.encrypt(plain_text)
	print(cipher_text)
	print(v.decrypt(cipher_text))
	
	
	
	
	
	

if __name__ == "__main__":
	main()
	
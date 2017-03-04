from CipherInterface import *
import math

class Caesar(CipherInterface):
	def __init__(self):
		CipherInterface.__init__(self)
		
	def setKey(self, key):
		self.key = key
		
	def encrypt(self, plain_text):
		cipher_text = ""
		
		for char in plain_text:
			encrypt_letter = ord(char) + self.key
			if encrypt_letter > 96 and encrypt_letter < 123:
				cipher_text += chr(encrypt_letter)
			
			else:
				remainder = (encrypt_letter  - 123) % 26
				encrypt_letter = 97 + remainder
				cipher_text += chr(encrypt_letter)
					
		return cipher_text
	
	def decrypt(self, cipher_text):
		plain_text = ""
		
		for char in cipher_text:
			decrypt_letter = ord(char) - self.key
			if decrypt_letter > 96 and decrypt_letter < 123:
				plain_text += chr(decrypt_letter)
			
			else:
				remainder = int(math.fabs(decrypt_letter  - 97) % 26)
				decrypt_letter = 123 - remainder
				plain_text += chr(decrypt_letter)
					
		return plain_text
		
		
		
def main():
	c = Caesar()
	c.setKey(3)
	
	letters = "abcdefghwxyz"
	cipher_text = c.encrypt(letters)
	print(cipher_text)
	plain_text = c.decrypt(cipher_text)
	print(plain_text)
	

if __name__ == "__main__":
	main()
	
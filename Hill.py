from CipherInterface import *
import numpy as np
import math

class Hill(CipherInterface):
	def __init__(self, size):
		CipherInterface.__init__(self)
		self.alphabet = self.create_alphabet()
		self.size = size
		
	def setKey(self, key):
		self.key = key
		
	def encrypt(self, plain_text):
		cipher_text = ""
		
		self.key = self.convert_letters_to_list(self.key)
		
		self.key = self.convert_list_to_matrix(self.key)

		plain_matrix = self.convert_letters_to_list(plain_text)
		
		plain_matrix = self.convert_list_to_matrix(plain_matrix)
	

		for section in plain_matrix:
			cipher_matrix = np.matmul(self.key, section) % 26
			cipher_text = self.convert_matrix_to_letters(cipher_text, cipher_matrix)
		
		return cipher_text
	
	def decrypt(self, cipher_text):
		plain_text = ""
		
		self.key = self.convert_letters_to_list(self.key)
		
		self.key = self.convert_list_to_matrix(self.key)
		
		cipher_matrix = self.convert_letters_to_list(cipher_text)
		
		cipher_matrix = self.convert_list_to_matrix(cipher_matrix)
		
		print(self.key)
		#print(self.key)
		inverted_matrix = (np.linalg.inv(self.key) % 26)  
		print(inverted_matrix)
		
		#inverted_matrix = inverted_matrix.astype(int)
		#print(cipher_matrix)
		#print(inverted_matrix)
		#print(np.matmul(cipher_matrix, inverted_matrix))
		#print(inverted_matrix)
		for section in cipher_matrix:
			#print(section)
			plain_matrix = np.matmul(inverted_matrix, section) % 26
			#print(plain_matrix)
			plain_text = self.convert_matrix_to_letters(plain_text, plain_matrix)
			
		print(plain_text)
		
			
		return plain_text
	
	
	def convert_matrix_to_letters(self, cipher_text, matrix):
		for char in matrix:
			cipher_text += self.alphabet[char]
				
		return cipher_text
				
	
	def convert_letters_to_list(self, plain_text):
		total_list = []
		temp_list = []
		counter = 0
		
		for char in plain_text:
			counter += 1
			temp_list.append(char)
			
			if counter == self.size:
				t = temp_list.copy()
				total_list.append(t)
				counter = 0
				temp_list.clear()
		
		
		return total_list
		
		
	def convert_list_to_matrix(self, array):
		for key in array:
			for single in range(len(key)):
				key[single] = self.alphabet.index(key[single])
		
		return np.array(array)
		
	
	
	def create_alphabet(self):
		alphabet_list = []
		
		for ascii_val in range(97, 123):
			alphabet_list.append(chr(ascii_val))
		
		
		return alphabet_list	
		
def main():
	a = "gybnqkurp"
	#for char in a:
	#	print(ord(char) - ord('a'))
	
	h = Hill(math.sqrt(len(a)))
	word = "catcoozoo"

	h.setKey(a)
	e = h.encrypt(word)
	#print(e)
	
	q = Hill(math.sqrt(len(a)))
	q.setKey(a)
	g = q.decrypt(e)
	
	#n = np.array([[2,3], [5,7]])

	#print(np.linalg.inv(n) % 26)
	
if __name__ == "__main__":
	main()
	
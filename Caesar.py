from CipherInterface import *

class Caesar(CipherInterface):
	def __init__(self):
		CipherInterface.__init__(self)
		
	def setKey(self, key):
		self.key = key
		
	def encrypt(self, plain_text):
		pass
	
	def decrypt(self, cipher_text):
		pass
		
		
		
def main():
	c = Caesar()
	c.setKey("KEY")
	
	key = 3
	first = ord('z') + key
	
	if first > 96 and first < 123:
		second = chr(first)
		print(second)
	else:
		remainder = (first + key) - 123
		print(remainder)
	
	
	
	
	

if __name__ == "__main__":
	main()
	
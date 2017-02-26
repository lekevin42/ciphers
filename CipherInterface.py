class CipherInterface:
	def __init__(self):
		self.key = None
		
	def setKey(self, key):
		raise NotImplementedError("UNDEFINED SETKEY")
		
	def encrypt(self, plain_text):
		raise NotImplementedError("UNDEFINED ENCRYPT")
		
	def decrypt(self, cipher_text):
		raise NotImplementedError("UNDEFINED DECRYPT")
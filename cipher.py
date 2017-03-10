#Authors: Kevin Le, Michael Ha, Edwin Diaz
#python cipher.py <CIPHER NAME> <KEY> <ENC/DEC> <INPUTFILE> <OUTPUTFILE>
#Example run: python cipher.py vig same enc input.txt output.txt

import sys
from Caesar import *
from Vigenere import *
from Railfence import *
from RowTransposition import *

#read the contents of a file
def read_file(input_file):
	with open(input_file, "r") as file:
		contents = file.readline()
		
	return contents

#write the contents of a file
def write_file(output_file, cipher_text):
	with open(output_file, "w") as file:
		file.write(cipher_text)

#choose a cipher		
def choose_cipher(cipher_name, key, option, input_file, output_file):
	#Playfair 
	if cipher_name == "PLF":
		if option == "ENC":
			pass
		
		elif option == "DEC":
			pass
		
		else:
			print("Invalid option! Options are ENC/DEC")
	
	#Row Transposition
	elif cipher_name == "RTS":
		rowtransposition = RowTransposition()
		rowtransposition.setKey(key)
	
		if option == "ENC":
			plain_text = read_file(input_file)
			cipher_text = rowtransposition.encrypt(plain_text)
			write_file(output_file, cipher_text)
		
		elif option == "DEC":
			cipher_text = read_file(input_file)
			plain_text = rowtransposition.decrypt(cipher_text)
			write_file(output_file, plain_text)
		
		else:
			print("Invalid option! Options are ENC/DEC")
	
	#Railfence
	elif cipher_name == "RFC":
		railfence = Railfence()
		railfence.setKey(key)
	
		if option == "ENC":
			plain_text = read_file(input_file)
			cipher_text = railfence.encrypt(plain_text)
			write_file(output_file, cipher_text)
		
		elif option == "DEC":
			cipher_text = read_file(input_file)
			plain_text = railfence.decrypt(cipher_text)
			write_file(output_file, plain_text)
		
		else:
			print("Invalid option! Options are ENC/DEC")
	
	#Vigenere
	elif cipher_name == "VIG":
		vigenere = Vigenere()
		vigenere.setKey(key)
		
		if option == "ENC":
			plain_text = read_file(input_file)
			cipher_text = vigenere.encrypt(plain_text)
			write_file(output_file, cipher_text)
		
		elif option == "DEC":
			cipher_text = read_file(input_file)
			plain_text = vigenere.decrypt(cipher_text)
			write_file(output_file, plain_text)
		
		else:
			print("Invalid option! Options are ENC/DEC")
	
	#Caesar
	elif cipher_name == "CES":
		caesar = Caesar()
		caesar.setKey(int(key))
		
		if option == "ENC":
			plain_text = read_file(input_file)
			cipher_text = caesar.encrypt(plain_text)
			write_file(output_file, cipher_text)
			
		elif option == "DEC":
			cipher_text = read_file(input_file)
			plain_text = caesar.decrypt(cipher_text)
			write_file(output_file, plain_text)
			
		else:
			print("Invalid option! Options are ENC/DEC")
			
	else:
		print("Invalid cipher name chosen!")

def main():
	if len(sys.argv) == 6:
		cipher_name = sys.argv[1].upper()
		key = sys.argv[2].lower()
		option = sys.argv[3].upper()
		input_file = sys.argv[4].strip()
		output_file = sys.argv[5].strip()
		
	else:
		print("Invalid amount of arguments!")
		return
	
	choose_cipher(cipher_name, key, option, input_file, output_file)
	

if __name__ == "__main__":
	main()
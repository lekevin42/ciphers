import sys

def read_file(input_file):
	with open(input_file, "r") as file:
		contents = file.readline()
		
	return contents

def choose_cipher(cipher_name, key, option, input_file):
	plain_text = read_file(input_file)
	
	if cipher_name == "Playfair":
		pass
	
	elif cipher_name == "Row Transposition":
		pass
	
	elif cipher_name == "Railfence":
		pass
	
	elif cipher_name == "Vigenre":
		pass
	
	elif cipher_name == "Caesar":
		pass
	
	else:
		print("Invalid cipher name chosen!")

def main():
	if len(sys.argv) == 6:
		cipher_name = sys.argv[1]
		key = sys.argv[2]
		option = sys.argv[3]
		input_file = sys.argv[4]
		output_file = sys.argv[5]
		
	else:
		print("Invalid amount of arguments!")
		return
	
	choose_cipher(cipher_name, key, option, input_file)
	

if __name__ == "__main__":
	main()
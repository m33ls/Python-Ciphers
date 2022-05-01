alphabet='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

def cipher(text, key):
	ciphertext = ""
	key = key.lower()
	text = text.replace(" ", "").lower() # Make it work without doing this

	while (len(key) < len(text)):
		key += key
	# print(key)

	for i in range(len(text)):
		if alphabet.find(text[i]) == -1:
			ciphertext += text[i]
		else:
			ciphertext += ( alphabet[ alphabet.find(text[i]) + alphabet.find(key[i]) ] )

	return ciphertext

def decipher(text, key):
	ciphertext = ""
	key = key.lower()
	text = text.replace(" ", "").lower() # Make it work without doing this

	while (len(key) < len(text)):
		key += key
	# print(key)

	for i in range(len(text)):
		if alphabet.find(text[i]) == -1:
			ciphertext += text[i]
		else:
			ciphertext += ( alphabet[ alphabet.find(text[i]) - alphabet.find(key[i]) ] )

	return ciphertext

# Tests
print(cipher("Hello World!", "TestKey"))
print(cipher("The quick brown fox jumps over the lazy dog", "TestKey"))
print(decipher("Aidey Amkpv!", "TestKey"))
print(decipher("Mlw jemad fjhgr dhb bnwtq hzwk dlc eerr nse", "TestKey"))

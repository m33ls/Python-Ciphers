alphabet='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

def cipher(text, rotations):
	ciphertext = ""

	for i in text.lower():
		if alphabet.find(i) == -1:
			ciphertext += i
		else:
			ciphertext += alphabet[alphabet.find(i) + rotations]

	return ciphertext


def decipher(ciphertext, rotations):
	text = ""

	for i in ciphertext.lower():
		if alphabet.find(i) == -1:
			text += i
		else:
			text += alphabet[alphabet.find(i) - rotations]

	return text

# Tests
print(cipher("Hello World!", 13))
print(cipher("The quick brown fox jumps over the lazy dog", 13))

print(decipher("uryyb jbeyq!", 13))
print(decipher("gur dhvpx oebja sbk whzcf bire gur ynml qbt", 13))
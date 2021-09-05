from crypto.utils import alphabetOnly


class Playfair:
	def encrypt(plaintext, key):
		plaintext = alphabetOnly(plaintext)
		_key = key + "ABCDEFGHIKLMNOPQRSTUVWXYZ"
		_key = list(dict.fromkeys(_key))
		string = ""
		ciphertext = ""
		for i in range(len(plaintext)):
			if i == len(plaintext) - 1:
				string += plaintext[i]
			else:
				string += plaintext[i] + \
					("X" if plaintext[i] == plaintext[i + 1] else "")
		if len(string) % 2 == 1:
				string += "X"
		for i in range(0, len(string), 2):
			c1 = string[i] if string[i] != "J" else "I"
			c2 = string[i + 1] if string[i + 1] != "J" else "I"
			c1_i = _key.index(c1)
			c2_i = _key.index(c2)
			p1 = (c1_i // 5, c1_i % 5)
			p2 = (c2_i // 5, c2_i % 5)
			if p1[0] == p2[0]:
					ciphertext += _key[p1[0] * 5 +
															((p1[1] + 1) % 5)] + _key[p2[0] * 5 + ((p2[1] + 1) % 5)]
			elif p1[1] == p2[1]:
					ciphertext += _key[((p1[0] + 1) % 5) * 5 + p1[1]] + \
							_key[((p2[0] + 1) % 5) * 5 + p2[1]]
			else:
					ciphertext += _key[p1[0] * 5 + p2[1]] + _key[p2[0] * 5 + p1[1]]
		return ciphertext

	def decrypt(ciphertext, key):
		ciphertext = alphabetOnly(ciphertext)
		_key = key + "ABCDEFGHIKLMNOPQRSTUVWXYZ"
		_key = list(dict.fromkeys(_key))
		decrypttext = ""
		for i in range(0, len(ciphertext), 2):
			c1 = ciphertext[i] if ciphertext[i] != "J" else "I"
			c2 = ciphertext[i + 1] if ciphertext[i + 1] != "J" else "I"
			c1_i = _key.index(c1)
			c2_i = _key.index(c2)
			p1 = (c1_i // 5, c1_i % 5)
			p2 = (c2_i // 5, c2_i % 5)
			if p1[0] == p2[0]:
				decrypttext += _key[p1[0] * 5 +
														((p1[1] - 1) % 5)] + _key[p2[0] * 5 + ((p2[1] - 1) % 5)]
			elif p1[1] == p2[1]:
				decrypttext += _key[((p1[0] - 1) % 5) * 5 + p1[1]] + \
						_key[((p2[0] - 1) % 5) * 5 + p2[1]]
			else:
				decrypttext += _key[p1[0] * 5 + p2[1]] + \
						_key[p2[0] * 5 + p1[1]]
		return decrypttext

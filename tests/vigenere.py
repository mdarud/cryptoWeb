class Vigenere:
  def encrypt(plaintext, key):
    ciphertext = []
    for i in range(len(plaintext)):
      c = (ord(plaintext[i]) + ord(key[i % len(key)]) - ord("A") * 2) % 26
      c += ord("A")
      ciphertext.append(chr(c))
    return "".join(ciphertext)
  
  def decrypt(ciphertext, key):
    decrypttext = []
    for i in range(len(ciphertext)):
      c = (ord(ciphertext[i]) - ord(key[i % len(key)])) % 26
      c += ord("A")
      decrypttext.append(chr(c))
    return "".join(decrypttext)
class ExVigenere:
  def encrypt(plaintext, key):
    ciphertext = []
    for i in range(len(plaintext)):
      c = (ord(plaintext[i]) + ord(key[i % len(key)])) % 256
      ciphertext.append(chr(c))
    return "".join(ciphertext)
  
  def decrypt(ciphertext, key):
    decrypttext = []
    for i in range(len(ciphertext)):
      c = (ord(ciphertext[i]) - ord(key[i % len(key)])) % 256
      decrypttext.append(chr(c))
    return "".join(decrypttext)
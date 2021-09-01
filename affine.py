class Affine:
  def encrypt(plaintext, m, b):
    ciphertext = ""
    for i in range(len(plaintext)):
      ciphertext += chr((m * (ord(plaintext[i]) - ord("A")) + b) % 26 + ord("A"))
    return ciphertext
  
  def decrypt(ciphertext, m, b):
    x = 0
    while (m * x) % 26 != 1:
      x += 1

    decrypttext = ""
    for i in range(len(ciphertext)):
      decrypttext += chr((x * (ord(ciphertext[i]) - ord("A") - b)) % 26 + ord("A"))
    return decrypttext
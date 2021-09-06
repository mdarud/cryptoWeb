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
  
  def binencrypt(plainbin, key):
        cipherbin = bytes()
        for i, bin in enumerate(plainbin):
            cipherbin += ((bin + ord(key[i % len(key)])) %
                          256).to_bytes(1, "big")
        return cipherbin

  def bindecrypt(cipherbin, key):
      decryptbin = bytes()
      for i, bin in enumerate(cipherbin):
          decryptbin += ((bin - ord(key[i % len(key)])) %
                          256).to_bytes(1, "big")
      return decryptbin
import random
from crypto.utils import alphabetOnly


class FullVigenere:
  def encrypt(plaintext, key, seed=0):
    plaintext = alphabetOnly(plaintext)
    random.seed(seed)
    letter_list = list("ABCDEFGHJKLMNOPQRSTUVWXYZ")
    table = []
    ciphertext = ""
    for _ in range(26):
      table.append(random.sample(letter_list, len(letter_list)))
    for i in range(len(plaintext)):
      r = (ord(key[i]) - ord("A")) if i < len(key) else (
          ord(ciphertext[i - len(key)]) - ord("A"))
      c = ord(plaintext[i]) - ord("A")
      ciphertext += table[r][c]
    return ciphertext

  def decrypt(ciphertext, key, seed=0):
    ciphertext = alphabetOnly(ciphertext)
    random.seed(seed)
    letter_list = list("ABCDEFGHJKLMNOPQRSTUVWXYZ")
    table = []
    decrypttext = ""
    for _ in range(26):
      table.append(random.sample(letter_list, len(letter_list)))
    for i in range(len(ciphertext)):
      r = (ord(key[i]) - ord("A")) if i < len(key) else (
          ord(ciphertext[i - len(key)]) - ord("A"))
      c = table[r].index(ciphertext[i])
      decrypttext += chr(c + ord("A"))
    return decrypttext

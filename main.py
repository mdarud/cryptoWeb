from vigenere import Vigenere
from fullvigenere import FullVigenere
from autokeyvigenere import AutoVigenere
from exvigenere import ExVigenere
from playfair import Playfair
from affine import Affine
from enigma import Enigma

string = "dCodeVigenere".upper()
key = "ASD"
cipher = Vigenere.encrypt(string, key)
print(cipher)
print(Vigenere.decrypt(cipher, key))

string = "dCodeFullVigenere".upper()
key = "ASD"
cipher = FullVigenere.encrypt(string, key)
print(cipher)
print(FullVigenere.decrypt(cipher, key))

string = "dCodeAutoclave".upper()
key = "ASD"
cipher = AutoVigenere.encrypt(string, key)
print(cipher)
print(AutoVigenere.decrypt(cipher, key))

string = "dCodeExVigenere".upper()
key = "ASD"
cipher = ExVigenere.encrypt(string, key)
print(cipher)
print(ExVigenere.decrypt(cipher, key))

string = "dCodePlayfair".upper()
key = "ASD"
cipher = Playfair.encrypt(string, key)
print(cipher)
print(Playfair.decrypt(cipher, key))

string = "dCodeAffine".upper()
key = "ASD"
cipher = Affine.encrypt(string, 3, 1)
print(cipher)
print(Affine.decrypt(cipher, 3, 1))

string = "dCodeEnigma".upper()
e = Enigma()
e.set_used_rotor([1, 3, 4])
e.set_setting([ord("B") - ord("A"), ord("U") - ord("A"), ord("L") - ord("A")])
e.set_plug_setting("AV BS CG DL FU HZ IN KM OW RX")
cipher = e.encrypt(string)
print(cipher)
e.reset_setting()
e.set_setting([ord("B") - ord("A"), ord("U") - ord("A"), ord("L") - ord("A")])
print(e.encrypt(cipher))

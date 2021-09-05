import re
from flask import Flask, render_template, request
from crypto.vigenere import Vigenere
from crypto.fullvigenere import FullVigenere
from crypto.autokeyvigenere import AutoVigenere
from crypto.exvigenere import ExVigenere
from crypto.playfair import Playfair
from crypto.affine import Affine
from crypto.enigma import Enigma

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

def encrypt(plaintext, key, method):
    if (method == "vigenere"):
        plaintext = plaintext.upper()
        cipher = Vigenere.encrypt(plaintext, key)
    elif (method == "fullvigenere"):
        plaintext = plaintext.upper()
        cipher = FullVigenere.encrypt(plaintext, key)
    elif (method == "autokeyvigenere"):
        plaintext = plaintext.upper()
        cipher = AutoVigenere.encrypt(plaintext, key)
    elif (method == "exvigenere"):
        cipher = ExVigenere.encrypt(plaintext, key)
    elif (method == "playfair"):
        plaintext = plaintext.upper()
        cipher = Playfair.encrypt(plaintext, key)
    elif (method == "affine"):
        plaintext = plaintext.upper()
        cipher = Affine.encrypt(plaintext, key[0], key[1])
    elif (method == "enigma"):
        plaintext = plaintext.upper()
        cipher = Vigenere.encrypt(plaintext, key)
    else:
        cipher = "error"
    return cipher

def decrypt(cipher, key, method):
    if (method == "vigenere"):
        cipher = cipher.upper()
        plaintext = Vigenere.decrypt(cipher, key)
    return plaintext

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/encrypt", methods=["POST"])
def encryptMethod():
    req = request.form
    print(req)
    text = req["text"]
    method = req["method"]
    if (method == "affine"):
        keyA = int(req["keyA"])
        keyB = int(req["keyB"])
        key = [keyA, keyB]
    else:
        key = req["key"]
    cipher = encrypt(text,key,method)
    print(text)
    print(cipher)
    return render_template('index.html', output=cipher)

@app.route("/decrypt", methods=["POST"])
def decryptMethod():
    req = request.form
    print(req)
    text = req["text"]
    key = req["key"]
    method = req["method"]
    plaintext = decrypt(text,key,method)
    print(text)
    return render_template('index.html', output=plaintext)

if __name__ == '__main__':
    app.run()

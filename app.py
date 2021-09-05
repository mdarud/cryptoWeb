import os
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
    elif (method == "fullvigenere"):
        cipher = cipher.upper()
        plaintext = FullVigenere.decrypt(cipher, key)
    elif (method == "autokeyvigenere"):
        cipher = cipher.upper()
        plaintext = AutoVigenere.decrypt(cipher, key)
    elif (method == "exvigenere"):
        plaintext = ExVigenere.decrypt(cipher, key)
    elif (method == "playfair"):
        cipher = cipher.upper()
        plaintext = Playfair.decrypt(cipher, key)
    elif (method == "affine"):
        cipher = cipher.upper()
        plaintext = Affine.decrypt(cipher, key[0], key[1])
    elif (method == "enigma"):
        cipher = cipher.upper()
        plaintext = Vigenere.decrypt(cipher, key)
    else:
        plaintext = "error"
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

@app.route("/encrypt-file", methods=["POST"])
def encryptFileMethod():
    req = request.form
    print(req)
    f = request.files['file'] 
    if f.filename != '': 
        f.save(f.filename) 
    file = open(f.filename, "r")
    text = file.read()
    method = req["method"]
    if (method == "affine"):
        keyA = int(req["keyA"])
        keyB = int(req["keyB"])
        key = [keyA, keyB]
    else:
        key = req["key"]
    cipher = encrypt(text,key,method)
    os.remove(f.filename)
    return render_template('index.html', output=cipher)

@app.route("/decrypt", methods=["POST"])
def decryptMethod():
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
    plaintext = decrypt(text,key,method)
    print(text)
    return render_template('index.html', output=plaintext)

if __name__ == '__main__':
    app.run()

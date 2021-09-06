import os
from crypto.utils import guessExt
from flask import Flask, render_template, request, send_file
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

filetype = "text"


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


def methodName(method):
    if (method == "vigenere"):
        text = "Vigenere Cipher"
    elif (method == "fullvigenere"):
        text = "Full Vigenere Cipher"
    elif (method == "autokeyvigenere"):
        text = "Auto Key Vigenere Cipher"
    elif (method == "exvigenere"):
        text = "Extended Vigenere Cipher"
    elif (method == "playfair"):
        text = "Playfair Cipher"
    elif (method == "affine"):
        text = "Affine Cipher"
    elif (method == "enigma"):
        text = "Enigma Cipher"
    else:
        text = "error"
    return text


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/encrypt", methods=["POST"])
def encryptMethod():
    global attc
    attc = "EncryptedText.txt"
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
    cipher = encrypt(text, key, method)
    print(text)
    print(cipher)
    method = methodName(method)
    f = open(attc, "w")
    f.write(cipher)
    f.close()
    global flag
    flag = 0
    return render_template('index.html', input=text, method=method+" - Text (Encrypt)", output=cipher)


@app.route("/encrypt-file", methods=["POST"])
def encryptFileMethod():
    global attc
    req = request.form
    print(req)
    f = request.files['file']
    method = req["method"]
    filetype = req["filetype"]
    if f.filename != '':
        f.save(f.filename)
    if (filetype == "text"):
        file = open(f.filename, "r")
        text = file.read()
        method = req["method"]
        if (method == "affine"):
            keyA = int(req["keyA"])
            keyB = int(req["keyB"])
            key = [keyA, keyB]
        else:
            key = req["key"]
        cipher = encrypt(text, key, method)
        file.close()
        method = methodName(method)
        attc = f.filename.split(".")[0] + "-Encrypted.txt"
        fi = open(attc, "w")
        fi.write(cipher)
        fi.close()
    elif (filetype == "binary"):
        file = open(f.filename, "rb")
        bytes = file.read()
        text = bytes.decode("utf-8", "ignore")
        if (method == "affine"):
            keyA = int(req["keyA"])
            keyB = int(req["keyB"])
            key = [keyA, keyB]
        else:
            key = req["key"]
        cipher = encrypt(text, key, method)
        file.close()
        method = methodName(method)
        attc = f.filename.split(".")[0]
        content = cipher.encode("utf-8", "ignore")
        fi = open(attc, 'wb')
        fi.write(content)
        fi.close()
        return render_template('index.html', input=text[:100], method=method+" - File (Encrypt)", output=cipher[:100])
    else:
        text = "error"
        cipher = "error"
        method = methodName(method)
    os.remove(f.filename)
    return render_template('index.html', input=text, method=method+" - File (Encrypt)", output=cipher)


@app.route("/decrypt", methods=["POST"])
def decryptMethod():
    global attc
    attc = "DecryptedText.txt"
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
    plaintext = decrypt(text, key, method)
    print(text)
    method = methodName(method)
    f = open(attc, "w")
    f.write(plaintext)
    f.close()
    return render_template('index.html', input=text, method=method+" - Text (Decrypt)", output=plaintext)


@app.route("/decrypt-file", methods=["POST"])
def decryptFileMethod():
    global attc
    req = request.form
    print(req)
    f = request.files['file']
    method = req["method"]
    filetype = req["filetype"]
    if f.filename != '':
        f.save(f.filename)
    if (filetype == "text"):
        file = open(f.filename, "r")
        text = file.read()
        method = req["method"]
        if (method == "affine"):
            keyA = int(req["keyA"])
            keyB = int(req["keyB"])
            key = [keyA, keyB]
        else:
            key = req["key"]
        plaintext = decrypt(text, key, method)
        file.close()
        method = methodName(method)
        attc = f.filename.split(".")[0] + "-Decrypted.txt"
        fi = open(attc, "w")
        fi.write(plaintext)
        fi.close()
    elif (filetype == "binary"):
        file = open(f.filename, "rb")
        bytes = file.read()
        text = bytes.decode("utf-8", "ignore")
        if (method == "affine"):
            keyA = int(req["keyA"])
            keyB = int(req["keyB"])
            key = [keyA, keyB]
        else:
            key = req["key"]
        plaintext = decrypt(text, key, method)
        file.close()
        method = methodName(method)
        content = plaintext.encode("utf-8", "ignore")
        fa = open("temp", 'wb')
        fa.write(content)
        fa.close()
        attc = f.filename + guessExt("temp")
        print(attc)
        fi = open(attc, 'wb')
        fi.write(content)
        fi.close()
        return render_template('index.html', input=text[:100], method=method+" - File (Decrypt)", output=plaintext[:100])
    else:
        text = "error"
        cipher = "error"
        method = methodName(method)
    os.remove(f.filename)
    return render_template('index.html', input=text, method=method+" - File (Decrypt)", output=plaintext)


@app.route('/download')
def downloadFile():
    path = attc
    print(attc)
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run()

rotor_wiring = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE",
                "BDFHJLCPRTXVZNYEIWGAKMUSQO", "ESOVPZJAYQUIRHXLNFTGKDCMWB",
                "VZBRGITYUPSDNHLXAWMJQOFECK", "JPGVOUMFYQBENHZRDKASXLICTW",
                "NZJHGRCXMYSWBOUFAIVLPEKQDT", "FKQHTLXOCBJSPDZRAMEWNIUYGV"]
turnover_point = ["Q", "E", "V", "J", "Z", ["Z", "M"], ["Z", "M"], ["Z", "M"]]

reflector_wiring = ["YRUHQSLDPXNGOKMIEBFZCWVJAT", "FVPJIAOYEDRZXWGCTKUQSBNMHL"]


def generateRotor(i):
    return [ord(x) - ord("A") for x in rotor_wiring[i]]


def generateReflector(i):
    return [ord(x) - ord("A") for x in reflector_wiring[i]]


def generatePlug(string):
    default = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    usedChar = []
    plug_token = string.strip().upper().split(" ")
    for token in plug_token:
        if len(token) != 2:
            return default
        if token[0] == token[1]:
            return default
        if token[0] in usedChar or token[1] in usedChar:
            return default
        usedChar.append(token[0])
        usedChar.append(token[1])

    plug = default
    for token in plug_token:
        plug[ord(token[0]) - ord("A")] = token[1]
        plug[ord(token[1]) - ord("A")] = token[0]
    return plug


class Enigma:
    def __init__(self, n_rotor=3, used_rotor=[0, 1, 2], used_reflector=0, plug_setting=""):
        self.n_rotor = n_rotor
        self.used_rotor = used_rotor
        self.used_reflector = used_reflector
        self.plug_setting = plug_setting

        self.offset = [0 for _ in range(n_rotor)]  # rotor offset Grundstellung
        self.setting = [0 for _ in range(n_rotor)]  # Ringstellung
        self.turnover = [False for _ in range(n_rotor)]  # turnover state

        self.rotor = [generateRotor(i) for i in used_rotor]  # Walzenlage
        self.reflector = generateReflector(used_reflector)  # Umkehrwalze
        self.plug = generatePlug("")  # Steckerverbindungen

    def set_n_rotor(self, n_rotor):
        self.n_rotor = n_rotor

    def set_offset(self, offset):
        self.offset = offset

    def set_setting(self, setting):
        self.setting = setting

    def set_plug_setting(self, plug_setting):
        self.plug_setting = plug_setting
        self.plug = generatePlug(self.plug_setting)

    def set_used_rotor(self, used_rotor):
        if len(used_rotor) != self.n_rotor:
            return
        self.used_rotor = used_rotor
        self.rotor = [generateRotor(i) for i in used_rotor]

    def set_used_reflector(self, used_reflector):
        self.used_reflector = used_reflector
        self.reflector = generateReflector(used_reflector)

    def reset_setting(self):
        self.offset = [0 for _ in range(self.n_rotor)]  # rotor offset
        self.setting = [0 for _ in range(self.n_rotor)]  # Ringstellung
        self.turnover = [False for _ in range(self.n_rotor)]  # turnover state

    def encrypt(self, plaintext):
        ciphertext = ""
        self.turnover[-1] = True
        for x in plaintext:

            for i in reversed(range(self.n_rotor)):
                if self.turnover[i] == True:
                    self.offset[i] += 1
                    self.turnover[i] = False
                if self.offset[i] >= 26:
                    self.offset[i] = 0

            for i in reversed(range(self.n_rotor)):
                if i == self.n_rotor - 1:
                    self.turnover[i] = True
                if i > 0:
                    if self.used_rotor[i] < 5 and self.offset[i] == ord(turnover_point[self.used_rotor[i]]) - ord("A"):
                        self.turnover[i - 1] = True
                    elif self.used_rotor[i] >= 5:
                        if self.offset[i] == ord(turnover_point[self.used_rotor[i]][0]) - ord("A"):
                            self.turnover[i - 1] = True
                        if self.offset[i] == ord(turnover_point[self.used_rotor[i]][1]) - ord("A"):
                            self.turnover[i - 1] = True

            c = ord(self.plug[ord(x) - ord("A")]) - ord("A")

            # from right to left
            for i in reversed(range(self.n_rotor)):
                c = (self.rotor[i][(c - self.setting[i] + self.offset[i]) %
                                   26] + self.setting[i] - self.offset[i]) % 26

            c = self.reflector[c]

            # from left to right
            for i in range(self.n_rotor):
                c = (self.rotor[i].index((c - self.setting[i] + self.offset[i]) % 26) +
                     self.setting[i] - self.offset[i]) % 26

            c = self.plug[c]

            ciphertext += c

        return ciphertext

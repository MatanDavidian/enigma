from enigma import Enigma
from plugboard import Plugboard

e = Enigma()
p = Plugboard()
finish = int(input("Enter 1 to configure plug board, 0 to use the default plug board: "))
while finish:
    match = input("Enter a match (without space): ")
    p.connectPair(match[0], match[1])
    finish = int(input("Enter 0 to finish configure plug board, 1 to continue: "))

firstRotor = int(input("Enter The First Rotor Number: "))
firstKey = int(input("Enter The First Key(0 - 25): "))
secondRotor = int(input("Enter The Second Rotor Number: "))
secondKey = int(input("Enter The Second Key(0 - 25): "))
thirdRotor = int(input("Enter The Third Rotor Number: "))
thirdKey = int(input("Enter The Third Key(0 - 25): "))

e.machine_configuration_process(firstRotor, firstKey, secondRotor, secondKey, thirdRotor, thirdKey, p)

textToEncrypt = input("Enter A Text To Encrypt: ")
print("encrypt: " + textToEncrypt)
print("decrypt: ", end='')
e.complete_text_translation(textToEncrypt)

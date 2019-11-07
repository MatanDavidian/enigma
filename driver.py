from enigma import Enigma
from plugboard import Plugboard

e = Enigma()
p = Plugboard()

configure = int(input("Enter 1 to configure plug board, 0 to use the default plug board: "))
if configure:
    match = input("Enter a match (without space): ").split()
    for m in match:
        p.connectPair(m[0], m[1])

rightRotor = int(input("Enter The Right Rotor Number: "))
rightKey = int(input("Enter The Right Key(1 - 26): ")) - 1
rightRotorRingSetting = int(input("Enter The Right Rotor Ring Setting(1 - 26): ")) - 1
middleRotor = int(input("Enter The Middle Rotor Number: "))
middleKey = int(input("Enter The Middle Key(1 - 26): ")) - 1
middleRotorRingSetting = int(input("Enter The Middle Rotor Ring Setting(1 - 26): ")) - 1
leftRotor = int(input("Enter The Left Rotor Number: "))
leftKey = int(input("Enter The Left Key(1 - 26): ")) - 1
leftRotorRingSetting = int(input("Enter The Left Rotor Ring Setting(1 - 26): ")) - 1

e.machine_configuration_process(rightRotor, rightKey, rightRotorRingSetting, middleRotor, middleKey, middleRotorRingSetting,
                                leftRotor, leftKey, leftRotorRingSetting, p)

# fast configuration
# e.machine_configuration_process(4, 8, 5, 2, 3, 7, 1, 18, 2, p)

textToEncrypt = input("Enter A Text To Encrypt: ")
print("encrypt: " + textToEncrypt)
print("decrypt: ", end='')
e.complete_text_translation(textToEncrypt)

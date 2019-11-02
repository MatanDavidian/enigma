from enigma import Enigma
from plugboard import Plugboard

e = Enigma()
p = Plugboard()

finish = int(input("Enter 1 to configure plug board, 0 to use the default plug board: "))
while finish:
    match = input("Enter a match (without space): ")
    p.connectPair(match[0], match[1])
    finish = int(input("Enter 0 to finish configure plug board, 1 to continue: "))

rightRotor = int(input("Enter The Right Rotor Number: "))
rightKey = int(input("Enter The Right Key(0 - 25): ")) - 1
rightRotorRingSetting = int(input("Enter The Right Rotor Ring Setting(0 - 25): ")) - 1
middleRotor = int(input("Enter The Middle Rotor Number: "))
middleKey = int(input("Enter The Middle Key(0 - 25): ")) - 1
middleRotorRingSetting = int(input("Enter The Middle Rotor Ring Setting(0 - 25): ")) - 1
leftRotor = int(input("Enter The Left Rotor Number: "))
leftKey = int(input("Enter The Left Key(0 - 25): ")) - 1
leftRotorRingSetting = int(input("Enter The Left Rotor Ring Setting(0 - 25): ")) - 1

e.machine_configuration_process(rightRotor, rightKey, rightRotorRingSetting, middleRotor, middleKey, middleRotorRingSetting,
                                leftRotor, leftKey, leftRotorRingSetting, p)
# fast configuration
# e.machine_configuration_process(4, 8, 5, 2, 3, 7, 1, 18, 2, p)

textToEncrypt = input("Enter A Text To Encrypt: ")
print("encrypt: " + textToEncrypt)
print("decrypt: ", end='')
e.complete_text_translation(textToEncrypt)

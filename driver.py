from enigma import Enigma

e = Enigma()

firstRotor = int(input("Enter The First Rotor Number: "))
firstKey = int(input("Enter The First Key(0 - 25) Rotor Number: "))
secondRotor = int(input("Enter The Second Rotor Number: "))
secondKey = int(input("Enter The Second Key(0 - 25) Rotor Number: "))
thirdRotor = int(input("Enter The Third Rotor Number: "))
thirdKey = int(input("Enter The Third Key(0 - 25) Rotor Number: "))

e.machine_configuration_process(firstRotor, firstKey, secondRotor, secondKey, thirdRotor, thirdKey)

textToEncrypt = input("Enter A Text To Encrypt: ")
print("encrypt: " + textToEncrypt)
print("decrypt: ", end='')
e.complete_letter_translation(textToEncrypt)

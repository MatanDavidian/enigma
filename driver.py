from enigma import Enigma
from plugboard import Plugboard

e = Enigma()
p = Plugboard()
p.initials()
'''
configure = int(input("Enter 1 to configure plug board, 0 to use the default plug board: "))
if configure:
    count = 0
    match = input("Enter pairs - less than 10 pairs (for example: AB CD FK): ").split()
    for m in match:
        if count > 10:
            print("you entered more then 10 pairs, only the first 10 configured.")
            break
        p.connectPair(m[0], m[1])
        count += 1

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
'''
# fast configuration
# e.machine_configuration_process(4, 8, 5, 2, 3, 7, 1, 18, 2, p)

#textToEncrypt = input("Enter A Text To Encrypt: ")

for i in range(26):
    for j in range(26):
      for k in range(26):
        for m in range(5):
          p.connectPair('Z', 'U')
          p.connectPair('W', 'M')
          p.connectPair('H', 'L')
          p.connectPair('C', 'Q')
          p.connectPair('O', 'A')
          p.connectPair('P', 'Y')
          p.connectPair('E', 'B')
          p.connectPair('T', 'R')
          p.connectPair('D', 'N')
          p.connectPair('V', 'I')

          e.machine_configuration_process(1, i, j, 2, k, m, 3, 1, 1, p)
          e.complete_text_translation("AAAAAAAAAA")
          p.initials()

# for i in range(100000):
#     textToEncrypt = "HI MY NAME IS TOM"
#     #print("encrypt: " + textToEncrypt)
#     #print("decrypt: ", end='')
#     e.complete_text_translation(textToEncrypt)

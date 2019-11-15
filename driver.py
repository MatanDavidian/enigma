from enigma import Enigma
from plugboard import Plugboard

"""
			-**********************-
			*					   *
			*	 ENIGMA MACHINE    *
			*					   *
			-**********************-
			
			AUTHORS:		|  ID:
			--------		| -----
			MATAN DAVIDIAN  | 205509219
			TOM DAMRI		| 205770068
			Tomer Leon		| 312203003
			Alex Kreinis	| 312623218
							
			DATE : 	15.11.19
"""
e = Enigma()
p = Plugboard()
p.initials()
fast_configure = int(input("FOR FAST CONFIGURE PRESS 0 FOR COSTUME CONFIGURE PRESS 1: "))
if fast_configure == 1:
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
    #
    while True:
        rightRotor = int(input("Enter The Right Rotor Number(1-5): "))
        if 1 <= rightRotor <= 5:
            break
        else:
            print("ERROR, try again:", end=' ')
    #
    while True:
        rightKey = int(input("Enter The Right Key(0 - 25): ")) - 1
        if 0 <= rightKey <= 25:
            break
        else:
            print("ERROR, try again:", end=' ')
    #
    while True:
        rightRotorRingSetting = int(input("Enter The Right Rotor Ring Setting(0 - 25): ")) - 1
        if 0 <= rightRotorRingSetting <= 25:
            break
        else:
            print("ERROR, try again:", end=' ')
    #
    while True:
        middleRotor = int(input("Enter The Middle Rotor Number1-5): "))
        if 0 < middleRotor < 6 and middleRotor != rightRotor:
            break
        else:
            print("ERROR, try again:", end=' ')
    #
    while True:
        middleKey = int(input("Enter The Middle Key(0 - 25): ")) - 1
        if 0 <= middleKey <= 25:
            break
        else:
            print("ERROR, try again:", end=' ')
    #
    while True:
        middleRotorRingSetting = int(input("Enter The Middle Rotor Ring Setting(0 - 25): ")) - 1
        if 0 <= middleRotorRingSetting <= 25:
            break
        else:
            print("ERROR, try again:", end=' ')
    #
    while True:
        leftRotor = int(input("Enter The Left Rotor Number1-5): "))
        if 0 < leftRotor < 6 and leftRotor != rightRotor and leftRotor != middleRotor:
            break
        else:
            print("ERROR, try again:", end=' ')
    #
    while True:
        leftKey = int(input("Enter The Left Key(0 - 25): ")) - 1
        if 0 <= leftKey <= 25:
            break
        else:
            print("ERROR, try again:", end=' ')
    #
    while True:
        leftRotorRingSetting = int(input("Enter The Left Rotor Ring Setting(0 - 25): ")) - 1
        if 0 <= leftRotorRingSetting <= 25:
            break
        else:
            print("ERROR, try again:", end=' ')
    #
    e.machine_configuration_process(rightRotor, rightKey, rightRotorRingSetting, middleRotor, middleKey,
                                    middleRotorRingSetting,
                                    leftRotor, leftKey, leftRotorRingSetting, p)

    textToEncrypt = input("Enter A Text To Encrypt: ")
    print("encrypt: " + textToEncrypt)
    print("decrypt: ", end='')
    e.complete_text_translation(textToEncrypt)
elif fast_configure == 0:
    # fast configuration
    p.connectPair('Z', 'U')
    p.connectPair('W', 'M')
    p.connectPair('H', 'L')
    p.connectPair('C', 'Q')
    p.connectPair('O', 'A')
    p.connectPair('P', 'Y')
    p.connectPair('D', 'N')
    p.connectPair('V', 'I')
    p.connectPair('E', 'B')
    p.connectPair('T', 'R')
    e.machine_configuration_process(4, 13, 23,   5, 14, 8,   2, 2, 18, p)
    textToEncrypt = "MLD"
    print("encrypt: " + textToEncrypt)
    print("decrypt: ", end='')
    e.complete_text_translation(textToEncrypt)
else:
    print("next time chose 0 or 1")

# for checking performance
'''
for i in range(26):
    for j in range(26):
        for k in range(26):
            for m in range(26):

                p.connectPair('Z', 'U')
                p.connectPair('W', 'M')
                p.connectPair('H', 'L')
                p.connectPair('C', 'Q')
                p.connectPair('O', 'A')
                p.connectPair('P', 'Y')
                p.connectPair('D', 'N')
                p.connectPair('V', 'I')
                
                e.machine_configuration_process(1, i, j, 2, k, m, 3, 1, 2, p)
                e.complete_text_translation("AAAAAAAAAA")
                p.initials()
'''

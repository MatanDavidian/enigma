LETTER_A_IN_ASCII = 65
LETTER_Z_IN_ASCII = 91

# ROTOR_CONVERSION1= E   K   M  F   L  G  D  Q   V   Z   N   T   O   W    Y  H  X   U   S   P   A  I  B  R   C  J
ROTOR_CONVERSION1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
ROTOR_REVERSE_CONVERSION1 = [20, 22, 24, 6, 0, 3, 5, 15, 21, 25, 1, 4, 2, 10, 12, 19, 7, 23, 18, 11, 17, 8, 13, 16, 14, 9]
'''
       rotorReverseConversion1 = {'E': 0, 'K': 1, 'M': 2, 'F': 3, 'L': 4, 'G': 5, 'D': 6, 'Q': 7, 'V': 8, 'Z': 9
           , 'N': 10, 'T': 11, 'O': 12, 'W': 13, 'Y': 14, 'H': 15, 'X': 16, 'U': 17, 'S': 18
           , 'P': 19, 'A': 20, 'I': 21, 'B': 22, 'R': 23, 'C': 24, 'J': 25}
'''
# ROTOR_CONVERSION2= A  J  D   K   S  I   R   U   X  B   L  H   W   T  M   C   Q  G   Z   N   P   Y  F   V  O   E
ROTOR_CONVERSION2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
ROTOR_REVERSE_CONVERSION2 = [0, 9, 15, 2, 25, 22, 17, 11, 5, 1, 3, 10, 14, 19, 24, 20, 16, 6, 4, 13, 7, 23, 12, 8, 21, 18]
'''
       rotorReverseConversion2 = {'A': 0, 'J': 1, 'D': 2, 'K': 3, 'S': 4, 'I': 5, 'R': 6, 'U': 7, 'X': 8, 'B': 9
           , 'L': 10, 'H': 11, 'W': 12, 'T': 13, 'M': 14, 'C': 15, 'Q': 16, 'G': 17, 'Z': 18
           , 'N': 19, 'P': 20, 'Y': 21, 'F': 22, 'V': 23, 'O': 24, 'E': 25}
'''
# ROTOR_CONVERSION3= B  D  F  H  J   L  C  P   R   T   X   V   Z   N   Y   E  I   W  G  A   K  M   U   S   Q   O
ROTOR_CONVERSION3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
ROTOR_REVERSE_CONVERSION3 = [19, 0, 6, 1, 15, 2, 18, 3, 16, 4, 20, 5, 21, 13, 25, 7, 24, 8, 23, 9, 22, 11, 17, 10, 14, 12]
'''
        rotorReverseConversion3 = {'B': 0, 'D': 1, 'F': 2, 'H': 3, 'J': 4, 'L': 5, 'C': 6, 'P': 7, 'R': 8, 'T': 9
            , 'X': 10, 'V': 11, 'Z': 12, 'N': 13, 'Y': 14, 'E': 15, 'I': 16, 'W': 17, 'G': 18
            , 'A': 19, 'K': 20, 'M': 21, 'U': 22, 'S': 23, 'Q': 24, 'O': 25}
'''
# ROTOR_CONVERSION4= E   S   O   V   P   Z  J  A   Y   Q   U  I   R  H   X   L   N  F   T  G   K  D  C   M   W  B
ROTOR_CONVERSION4 = [4, 18, 14, 21, 15, 25, 9, 0, 24, 16, 20, 8, 17, 7, 23, 11, 13, 5, 19, 6, 10, 3, 2, 12, 22, 1]
ROTOR_REVERSE_CONVERSION4 = [7, 25, 22, 21, 0, 17, 19, 13, 11, 6, 20, 15, 23, 16, 2, 4, 9, 12, 1, 18, 10, 3, 24, 14, 8, 5]
'''
       rotorReverseConversion4 = {'E': 0, 'S': 1, 'O': 2, 'V': 3, 'P': 4, 'Z': 5, 'J': 6, 'A': 7, 'Y': 8, 'Q': 9,
                                  'U': 10, 'I': 11, 'R': 12, 'H': 13, 'X': 14, 'L': 15, 'N': 16, 'F': 17, 'T': 18,
                                  'G': 19, 'K': 20, 'D': 21, 'C': 22, 'M': 23, 'W': 24, 'B': 25}
'''

# ROTOR_CONVERSION5= V   Z   B   R  G  I   T   Y   U   P   S  D   N  H   L   X  A   W   M  J   Q   O  F  E  C   K
ROTOR_CONVERSION5 = [21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10]
ROTOR_REVERSE_CONVERSION5 = [16, 2, 24, 11, 23, 22, 4, 13, 5, 19, 25, 14, 18, 12, 21, 9, 20, 3, 10, 6, 8, 0, 17, 15, 7, 1]
'''
        rotorReverseConversion5 = {'V': 0, 'Z': 1, 'B': 2, 'R': 3, 'G': 4, 'I': 5, 'T': 6, 'Y': 7, 'U': 8, 'P': 9,
                                   'S': 10, 'D': 11, 'N': 12, 'H': 13, 'L': 14, 'X': 15, 'A': 16, 'W': 17, 'M': 18,
                                   'J': 19, 'Q': 20, 'O': 21, 'F': 22, 'E': 23, 'C': 24, 'K': 25}
'''

# REFLECTOR_CONVERSION= Y   R   U   H   Q   S   L  D   P   X   N  G   O  K   M   I  E  B  F   Z  C   W   V  J  A  T
REFLECTOR_CONVERSION = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]

ROTOR_CONVERSION = [ROTOR_CONVERSION1, ROTOR_CONVERSION2, ROTOR_CONVERSION3, ROTOR_CONVERSION4, ROTOR_CONVERSION5]
ROTOR_REVERSE_CONVERSION = [ROTOR_REVERSE_CONVERSION1, ROTOR_REVERSE_CONVERSION2, ROTOR_REVERSE_CONVERSION3, ROTOR_REVERSE_CONVERSION4, ROTOR_REVERSE_CONVERSION5]


from abc import ABC, abstractmethod
class Substitutor(ABC):
    rotorConversion1 = ['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y','H','X','U','S','P','A','I','B','R','C','J']
    rotorReverseConversion1 = {'E': 0,'K': 1,'M': 2,'F': 3,'L': 4,'G': 5,'D': 6,'Q': 7,'V': 8,'Z': 9
                                  ,'N': 10,'T': 11,'O': 12,'W': 13,'Y': 14,'H': 15,'X': 16,'U': 17,'S': 18
                                  ,'P': 19,'A': 20,'I': 21,'B': 22,'R': 23,'C': 24,'J': 25}
    rotorIndex1 = 0

    rotorConversion2 = ['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M','C','Q','G','Z','N','P','Y','F','V','O','E']

    rotorReverseConversion2 = {'A': 0, 'J': 1, 'D': 2, 'K': 3, 'S': 4, 'I': 5, 'R': 6, 'U': 7, 'X': 8, 'B': 9
        , 'L': 10, 'H': 11, 'W': 12, 'T': 13, 'M': 14, 'C': 15, 'Q': 16, 'G': 17, 'Z': 18
        , 'N': 19, 'P': 20, 'Y': 21, 'F': 22, 'V': 23, 'O': 24, 'E': 25}
    rotorIndex2 = 0

    rotorConversion3 = ['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y','E','I','W','G','A','K','M','U','S','Q','O']
    rotorReverseConversion3 = {'B': 0, 'D': 1, 'F': 2, 'H': 3, 'J': 4, 'L': 5, 'C': 6, 'P': 7, 'R': 8, 'T': 9
        , 'X': 10, 'V': 11, 'Z': 12, 'N': 13, 'Y': 14, 'E': 15, 'I': 16, 'W': 17, 'G': 18
        , 'A': 19, 'K': 20, 'M': 21, 'U': 22, 'S': 23, 'Q': 24, 'O': 25}
    rotorIndex3 = 0
    rotorConversion4 = ['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B']
    rotorReverseConversion4 = {'E': 0, 'S': 1, 'O': 2, 'V': 3, 'P': 4, 'Z': 5, 'J': 6, 'A': 7, 'Y': 8, 'Q': 9,
    'U': 10, 'I': 11, 'R': 12, 'H': 13, 'X': 14, 'L': 15, 'N': 16, 'F': 17, 'T': 18,
    'G': 19, 'K': 20, 'D': 21, 'C': 22, 'M': 23, 'W': 24, 'B': 25}
    rotorIndex4 = 0
    rotorConversion5 = ['V','Z','B','R','G','I','T','Y','U','P','S','D','N','H','L','X','A','W','M','J','Q','O','F','E','C','K']
    rotorReverseConversion5 = {'V': 0, 'Z': 1, 'B': 2, 'R': 3, 'G': 4, 'I': 5, 'T': 6, 'Y': 7, 'U': 8, 'P': 9,
                               'S': 10, 'D': 11, 'N': 12, 'H': 13, 'L': 14, 'X': 15, 'A': 16, 'W': 17, 'M': 18,
                               'J': 19, 'Q': 20, 'O': 21, 'F': 22, 'E': 23, 'C': 24, 'K': 25}
    rotorIndex5 = 0
    reflectorConversion = ['Y','R','U','H','Q','S','L','D','P','X','N','G','O','K','M','I','E','B','F','Z','C','W','V','J','A','T']
    plugBoard = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    def letter_index_conversions(self, char_input_num, rotor_num):
        #print(char_input_num)
        if rotor_num == 1:
            #print(self.rotorConversion1[(char_input_num + self.rotorIndex1) % 26])
            return ord(self.rotorConversion1[(char_input_num + self.rotorIndex1) % 26]) - 65 - self.rotorIndex1
        elif rotor_num == 2:
            #print(self.rotorConversion2[(char_input_num + self.rotorIndex2) % 26])
            return ord(self.rotorConversion2[(char_input_num + self.rotorIndex2) % 26]) - 65 - self.rotorIndex2
        elif rotor_num == 3:
            #print(self.rotorConversion3[(char_input_num + self.rotorIndex3) % 26])
            return ord(self.rotorConversion3[(char_input_num + self.rotorIndex3) % 26]) - 65 - self.rotorIndex3
        elif rotor_num == 4:
            #print(self.rotorConversion4[(char_input_num + self.rotorIndex4) % 26])
            return ord(self.rotorConversion4[(char_input_num + self.rotorIndex4) % 26]) - 65 - self.rotorIndex4
        elif rotor_num == 5:
            #print(self.rotorConversion5[(char_input_num + self.rotorIndex5) % 26])
            return ord(self.rotorConversion5[(char_input_num + self.rotorIndex5) % 26]) - 65 - self.rotorIndex5
        elif rotor_num == 6:
            return self.reflectorConversion[char_input_num] + 65

    def letter_index_reverse_conversions(self, char_input, rotor_num):
        if rotor_num == 1:
            return self.rotorReverseConversion1[chr((char_input - self.rotorIndex1) % 26 + 65)]
        elif rotor_num == 2:
            return self.rotorReverseConversion2[chr((char_input - self.rotorIndex2)%26 + 65)]
        elif rotor_num == 3:
            #print(chr((char_input - self.rotorIndex3)%26 + 65))
            return self.rotorReverseConversion3[chr((char_input - self.rotorIndex3)%26 + 65)]
        elif rotor_num == 4:
            #print(chr((char_input - self.rotorIndex4)%26 + 65))
            return self.rotorReverseConversion4[chr((char_input - self.rotorIndex4)%26 + 65)]
        elif rotor_num == 5:
            #print(chr((char_input + self.rotorIndex5)%26 + 65))
            return self.rotorReverseConversion5[chr((char_input + self.rotorIndex5)%26 + 65)] - self.rotorIndex5

    def circular_shift(self):
        if self.rotorIndex4 == 9:  # on j
            self.rotorIndex3 = (self.rotorIndex3 + 1) % 26
        if self.rotorIndex3 == 21:  # on v
            self.rotorIndex2 = (self.rotorIndex2 + 1) % 26
        if self.rotorIndex2 == 4:  # on e
            self.rotorIndex1 = (self.rotorIndex1 + 1) % 26

        self.rotorIndex5 = (self.rotorIndex5+1)%26
        if self.rotorIndex5 == 0: # move from z to a
            self.rotorIndex4 = (self.rotorIndex4 +1)%26

            if self.rotorIndex4 == 10:  # move from j to k
                self.rotorIndex3 = (self.rotorIndex3 + 1) % 26

                if self.rotorIndex3 == 22:  # move from v to w
                    self.rotorIndex2 = (self.rotorIndex2 + 1) % 26

                    if self.rotorIndex2 == 5:  # move from e to f
                        self.rotorIndex1 = (self.rotorIndex1 + 1) % 26

    def translation(self):
        pass

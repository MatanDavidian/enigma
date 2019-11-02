class Substitutor():

    def __init__(self):
        self.configured = False
        self.firstTurnoverNotch = 0
        self.secondTurnoverNotch = 0
        self.thirdTurnoverNotch = 0

        self.firstRotorIndex = 0
        self.secondRotorIndex = 0
        self.thirdRotorIndex = 0

        self.rotorConversion1 = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S',
                            'P', 'A', 'I', 'B', 'R', 'C', 'J']
        self.rotorReverseConversion1 = {'E': 0, 'K': 1, 'M': 2, 'F': 3, 'L': 4, 'G': 5, 'D': 6, 'Q': 7, 'V': 8, 'Z': 9
            , 'N': 10, 'T': 11, 'O': 12, 'W': 13, 'Y': 14, 'H': 15, 'X': 16, 'U': 17, 'S': 18
            , 'P': 19, 'A': 20, 'I': 21, 'B': 22, 'R': 23, 'C': 24, 'J': 25}

        self.rotorConversion2 = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z',
                            'N', 'P', 'Y', 'F', 'V', 'O', 'E']

        self.rotorReverseConversion2 = {'A': 0, 'J': 1, 'D': 2, 'K': 3, 'S': 4, 'I': 5, 'R': 6, 'U': 7, 'X': 8, 'B': 9
            , 'L': 10, 'H': 11, 'W': 12, 'T': 13, 'M': 14, 'C': 15, 'Q': 16, 'G': 17, 'Z': 18
            , 'N': 19, 'P': 20, 'Y': 21, 'F': 22, 'V': 23, 'O': 24, 'E': 25}

        self.rotorConversion3 = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I',
                            'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']
        self.rotorReverseConversion3 = {'B': 0, 'D': 1, 'F': 2, 'H': 3, 'J': 4, 'L': 5, 'C': 6, 'P': 7, 'R': 8, 'T': 9
            , 'X': 10, 'V': 11, 'Z': 12, 'N': 13, 'Y': 14, 'E': 15, 'I': 16, 'W': 17, 'G': 18
            , 'A': 19, 'K': 20, 'M': 21, 'U': 22, 'S': 23, 'Q': 24, 'O': 25}

        self.rotorConversion4 = ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T',
                            'G', 'K', 'D', 'C', 'M', 'W', 'B']
        self.rotorReverseConversion4 = {'E': 0, 'S': 1, 'O': 2, 'V': 3, 'P': 4, 'Z': 5, 'J': 6, 'A': 7, 'Y': 8, 'Q': 9,
                                   'U': 10, 'I': 11, 'R': 12, 'H': 13, 'X': 14, 'L': 15, 'N': 16, 'F': 17, 'T': 18,
                                   'G': 19, 'K': 20, 'D': 21, 'C': 22, 'M': 23, 'W': 24, 'B': 25}

        self.rotorConversion5 = ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M',
                            'J', 'Q', 'O', 'F', 'E', 'C', 'K']
        self.rotorReverseConversion5 = {'V': 0, 'Z': 1, 'B': 2, 'R': 3, 'G': 4, 'I': 5, 'T': 6, 'Y': 7, 'U': 8, 'P': 9,
                                   'S': 10, 'D': 11, 'N': 12, 'H': 13, 'L': 14, 'X': 15, 'A': 16, 'W': 17, 'M': 18,
                                   'J': 19, 'Q': 20, 'O': 21, 'F': 22, 'E': 23, 'C': 24, 'K': 25}

        self.reflectorConversion = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B',
                               'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']

    def set_rotor_order(self, first, second, third):
        if first == 1:
            self.firstTurnoverNotch = 17
        elif first == 2:
            self.firstTurnoverNotch = 5
        elif first == 3:
            self.firstTurnoverNotch = 22
        elif first == 4:
            self.firstTurnoverNotch = 10
        elif first == 5:
            self.firstTurnoverNotch = 0

        if second == 1:
            self.secondTurnoverNotch = 17
        elif second == 2:
            self.secondTurnoverNotch = 5
        elif second == 3:
            self.secondTurnoverNotch = 22
        elif second == 4:
            self.secondTurnoverNotch = 10
        elif second == 5:
            self.secondTurnoverNotch = 0

        if third == 1:
            self.thirdTurnoverNotch = 17
        elif third == 2:
            self.thirdTurnoverNotch = 5
        elif third == 3:
            self.thirdTurnoverNotch = 22
        elif third == 4:
            self.thirdTurnoverNotch = 10
        elif third == 5:
            self.thirdTurnoverNotch = 0

    def letter_index_conversions(self, char_input_num, rotor_num, rotor_index):
        # print(char_input_num)
        if rotor_num == 1:
            # print(self.rotorConversion1[(char_input_num + self.rotorIndex1) % 26])
            return (ord(self.rotorConversion1[(char_input_num + rotor_index) % 26]) - 65 - rotor_index) % 26
        elif rotor_num == 2:
            # print(self.rotorConversion2[(char_input_num + self.rotorIndex2) % 26])
            return (ord(self.rotorConversion2[(char_input_num + rotor_index) % 26]) - 65 - rotor_index) % 26
        elif rotor_num == 3:
            # print(self.rotorConversion3[(char_input_num + self.rotorIndex3) % 26])
            return (ord(self.rotorConversion3[(char_input_num + rotor_index) % 26]) - 65 - rotor_index) % 26
        elif rotor_num == 4:
            # print(self.rotorConversion4[(char_input_num + self.rotorIndex4) % 26])
            return (ord(self.rotorConversion4[(char_input_num + rotor_index) % 26]) - 65 - rotor_index) % 26
        elif rotor_num == 5:
            # print(self.rotorConversion5[(char_input_num + self.rotorIndex5) % 26])
            return (ord(self.rotorConversion5[(char_input_num + rotor_index) % 26]) - 65 - rotor_index) % 26
        elif rotor_num == 6:
            return self.reflectorConversion[char_input_num] + 65

    def letter_index_reverse_conversions(self, char_input, rotor_num, rotor_index):
        if rotor_num == 1:
            return (self.rotorReverseConversion1[chr((char_input + rotor_index) % 26 + 65)] - rotor_index) % 26
        elif rotor_num == 2:
            return (self.rotorReverseConversion2[chr((char_input + rotor_index) % 26 + 65)] - rotor_index) % 26
        elif rotor_num == 3:
            # print(chr((char_input + self.rotorIndex3)%26 + 65))
            return (self.rotorReverseConversion3[chr((char_input + rotor_index) % 26 + 65)] - rotor_index) % 26
        elif rotor_num == 4:
            # print(chr((char_input + self.rotorIndex4)%26 + 65))
            return (self.rotorReverseConversion4[chr((char_input + rotor_index) % 26 + 65)] - rotor_index) % 26
        elif rotor_num == 5:
            # print(chr((char_input + self.rotorIndex5)%26 + 65))
            return (self.rotorReverseConversion5[chr((char_input + rotor_index) % 26 + 65)] - rotor_index) % 26

    def circular_shift(self):
        if self.secondRotorIndex == self.secondTurnoverNotch - 1:
            self.thirdRotorIndex = (self.thirdRotorIndex + 1) % 26

        self.firstRotorIndex = (self.firstRotorIndex + 1) % 26

        if self.firstRotorIndex == self.firstTurnoverNotch:
            self.secondRotorIndex = (self.secondRotorIndex + 1) % 26
            if self.secondRotorIndex == self.secondTurnoverNotch:
                self.thirdRotorIndex = (self.thirdRotorIndex + 1) % 26
    def translation(self):
        pass

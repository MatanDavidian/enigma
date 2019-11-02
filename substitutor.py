class Substitutor():

    def __init__(self):
        self.configured = False
        self.firstTurnoverNotch = 0
        self.secondTurnoverNotch = 0
        self.thirdTurnoverNotch = 0

        self.firstRotorIndex = 0
        self.secondRotorIndex = 0
        self.thirdRotorIndex = 0

        self.rotorConversion1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18,
                            15, 0, 8, 1, 17, 2, 9]
        self.rotorReverseConversion1 = [20, 22, 24, 6, 0, 3, 5, 15, 21, 25, 1, 4, 2, 10, 12, 19, 7, 23, 18, 11, 17, 8,
                                        13, 16, 14, 9]
        '''
        self.rotorReverseConversion1 = {'E': 0, 'K': 1, 'M': 2, 'F': 3, 'L': 4, 'G': 5, 'D': 6, 'Q': 7, 'V': 8, 'Z': 9
            , 'N': 10, 'T': 11, 'O': 12, 'W': 13, 'Y': 14, 'H': 15, 'X': 16, 'U': 17, 'S': 18
            , 'P': 19, 'A': 20, 'I': 21, 'B': 22, 'R': 23, 'C': 24, 'J': 25}
        '''
        self.rotorConversion2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25,
                            13, 15, 24, 5, 21, 14, 4]
        self.rotorReverseConversion2 = [0, 9, 15, 2, 25, 22, 17, 11, 5, 1, 3, 10, 14, 19, 24, 20, 16, 6, 4, 13, 7, 23,
                                    12, 8, 21, 18]
        '''
        self.rotorReverseConversion2 = {'A': 0, 'J': 1, 'D': 2, 'K': 3, 'S': 4, 'I': 5, 'R': 6, 'U': 7, 'X': 8, 'B': 9
            , 'L': 10, 'H': 11, 'W': 12, 'T': 13, 'M': 14, 'C': 15, 'Q': 16, 'G': 17, 'Z': 18
            , 'N': 19, 'P': 20, 'Y': 21, 'F': 22, 'V': 23, 'O': 24, 'E': 25}
        '''
        self.rotorConversion3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8,
                            22, 6, 0, 10, 12, 20, 18, 16, 14]
        self.rotorReverseConversion3 = [19, 0, 6, 1, 15, 2, 18, 3, 16, 4, 20, 5, 21, 13, 25, 7, 24, 8, 23, 9, 22, 11,
                                        17, 10, 14, 12]
        '''
        self.rotorReverseConversion3 = {'B': 0, 'D': 1, 'F': 2, 'H': 3, 'J': 4, 'L': 5, 'C': 6, 'P': 7, 'R': 8, 'T': 9
            , 'X': 10, 'V': 11, 'Z': 12, 'N': 13, 'Y': 14, 'E': 15, 'I': 16, 'W': 17, 'G': 18
            , 'A': 19, 'K': 20, 'M': 21, 'U': 22, 'S': 23, 'Q': 24, 'O': 25}
        '''
        self.rotorConversion4 = [4, 18, 14, 21, 15, 25, 9, 0, 24, 16, 20, 8, 17, 7, 23, 11, 13, 5, 19,
                            6, 10, 3, 2, 12, 22, 1]
        # A in place 7, B in place 25 etc
        self.rotorReverseConversion4 = [7, 25, 22, 21, 0, 17, 19, 13, 11, 6, 20, 15, 23, 16, 2, 4, 9, 12, 1, 18, 10,
                                        3, 24, 14, 8, 5]
        '''
        self.rotorReverseConversion4 = {'E': 0, 'S': 1, 'O': 2, 'V': 3, 'P': 4, 'Z': 5, 'J': 6, 'A': 7, 'Y': 8, 'Q': 9,
                                   'U': 10, 'I': 11, 'R': 12, 'H': 13, 'X': 14, 'L': 15, 'N': 16, 'F': 17, 'T': 18,
                                   'G': 19, 'K': 20, 'D': 21, 'C': 22, 'M': 23, 'W': 24, 'B': 25}
        '''
        self.rotorConversion5 = [21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12,
                            9, 16, 14, 5, 4, 2, 10]
        self.rotorReverseConversion5 = [16, 2, 24, 11, 23, 22, 4, 13, 5, 19, 25, 14, 18, 12, 21, 9, 20, 3, 10, 6, 8,
                                        0, 17, 15, 7, 1]
        '''
        self.rotorReverseConversion5 = {'V': 0, 'Z': 1, 'B': 2, 'R': 3, 'G': 4, 'I': 5, 'T': 6, 'Y': 7, 'U': 8, 'P': 9,
                                   'S': 10, 'D': 11, 'N': 12, 'H': 13, 'L': 14, 'X': 15, 'A': 16, 'W': 17, 'M': 18,
                                   'J': 19, 'Q': 20, 'O': 21, 'F': 22, 'E': 23, 'C': 24, 'K': 25}
        '''
        self.reflectorConversion = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1,
                               5, 25, 2, 22, 21, 9, 0, 19]

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

    def letter_index_conversions(self, char_input_num, rotor_num, rotor_index, ring_setting):
        if rotor_num == 1:
            return (self.rotorConversion1[(char_input_num + rotor_index - ring_setting) % 26] - rotor_index + ring_setting) % 26
        elif rotor_num == 2:
            return (self.rotorConversion2[(char_input_num + rotor_index - ring_setting) % 26] - rotor_index + ring_setting) % 26
        elif rotor_num == 3:
            return (self.rotorConversion3[(char_input_num + rotor_index - ring_setting) % 26] - rotor_index + ring_setting) % 26
        elif rotor_num == 4:
            return (self.rotorConversion4[(char_input_num + rotor_index - ring_setting) % 26] - rotor_index + ring_setting) % 26
        elif rotor_num == 5:
            return (self.rotorConversion5[(char_input_num + rotor_index - ring_setting) % 26] - rotor_index + ring_setting) % 26

    def letter_index_reverse_conversions(self, char_input, rotor_num, rotor_index, ring_setting):
        if rotor_num == 1:
            return (self.rotorReverseConversion1[(char_input + rotor_index - ring_setting) % 26] - rotor_index + ring_setting) % 26
        elif rotor_num == 2:
            return (self.rotorReverseConversion2[(char_input + rotor_index - ring_setting) % 26] - rotor_index + ring_setting) % 26
        elif rotor_num == 3:
            return (self.rotorReverseConversion3[(char_input + rotor_index - ring_setting) % 26] - rotor_index + ring_setting) % 26
        elif rotor_num == 4:
            return (self.rotorReverseConversion4[(char_input + rotor_index - ring_setting) % 26] - rotor_index + ring_setting) % 26
        elif rotor_num == 5:
            return (self.rotorReverseConversion5[(char_input + rotor_index - ring_setting) % 26] - rotor_index + ring_setting) % 26

    def circular_shift(self):
        if self.firstRotorIndex == self.firstTurnoverNotch - 1 or self.secondRotorIndex == self.secondTurnoverNotch - 1:
            if self.secondRotorIndex == self.secondTurnoverNotch - 1:
                self.thirdRotorIndex = (self.thirdRotorIndex + 1) % 26
            self.secondRotorIndex = (self.secondRotorIndex + 1) % 26
        self.firstRotorIndex = (self.firstRotorIndex + 1) % 26
        '''
        if self.secondRotorIndex == self.secondTurnoverNotch - 1:
            self.secondRotorIndex = (self.secondRotorIndex + 1) % 26
            self.thirdRotorIndex = (self.thirdRotorIndex + 1) % 26

        self.firstRotorIndex = (self.firstRotorIndex + 1) % 26

        if self.firstRotorIndex == self.firstTurnoverNotch:
            self.secondRotorIndex = (self.secondRotorIndex + 1) % 26
            if self.secondRotorIndex == self.secondTurnoverNotch:
                self.thirdRotorIndex = (self.thirdRotorIndex + 1) % 26
        '''
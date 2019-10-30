from abc import ABC, abstractmethod
class Substitutor(ABC):
    rotorConversion1 = ['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y','H','X','U','S','P','A','I','B','R','C','J']
    rotorIndex1 = 0
    rotorConversion2 = ['A''J''D''K''S''I''R''U''X''B''L''H''W''T''M''C''Q''G''Z''N''P''Y''F''V''O''E']
    rotorIndex2 = 0
    rotorConversion3 = ['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y','E','I','W','G','A','K','M','U','S','Q','O']
    rotorIndex3 = 0
    rotorConversion4 = ['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B']
    rotorIndex4 = 0
    rotorConversion5 = ['V','Z','B','R','G','I','T','Y','U','P','S','D','N','H','L','X','A','W','M','J','Q','O','F','E','C','K']
    rotorIndex5 = 0
    reflectorConversion = ['Y','R','U','H','Q','S','L','D','P','X','N','G','O','K','M','I','E','B','F','Z','C','W','V','J','A','T']
    reflectorIndex = 0

    def letter_index_conversions(self, char_input, rotor_num):
        char_input -= 65
        if rotor_num == 1:
            return self.rotorConversion1[char_input]
        elif rotor_num == 2:
            return self.rotorConversion2[char_input]
        elif rotor_num == 3:
            return self.rotorConversion3[char_input]
        elif rotor_num == 4:
            return self.rotorConversion4[char_input]
        elif rotor_num == 5:
            return self.rotorConversion5[char_input]
        elif rotor_num == 6:
            return self.reflectorConversion[char_input]

    def circular_shift(self):
        if self.rotorIndex4 == 9:  # on j
            self.rotorIndex3 = (self.rotorIndex3 + 1) % 26
        if self.rotorIndex3 == 21:  # on v
            self.rotorIndex2 = (self.rotorIndex2 + 1) % 26
        if self.rotorIndex2 == 4:  # on e
            self.rotorIndex1 = (self.rotorIndex1 + 1) % 26

        self.rotorIndex5 = (self.rotorIndex1+5)%26
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

from consts import ROTOR_CONVERSION1 , ROTOR_CONVERSION2 , ROTOR_CONVERSION3 , ROTOR_CONVERSION4 , ROTOR_CONVERSION5
from consts import ROTOR_REVERSE_CONVERSION1 , ROTOR_REVERSE_CONVERSION2
from consts import ROTOR_REVERSE_CONVERSION3 , ROTOR_REVERSE_CONVERSION4 , ROTOR_REVERSE_CONVERSION5
from consts import REFLECTOR_CONVERSION

class Substitutor():
    def __init__(self):
        self.configured = False
        self.firstTurnoverNotch = 0
        self.secondTurnoverNotch = 0
        self.thirdTurnoverNotch = 0

        self.firstRotorIndex = 0
        self.secondRotorIndex = 0
        self.thirdRotorIndex = 0

        self.rotorConversion = [ROTOR_CONVERSION1, ROTOR_CONVERSION2, ROTOR_CONVERSION3, ROTOR_CONVERSION4, ROTOR_CONVERSION5]

        self.rotorReverseConversion = [ROTOR_REVERSE_CONVERSION1, ROTOR_REVERSE_CONVERSION2, ROTOR_REVERSE_CONVERSION3, ROTOR_REVERSE_CONVERSION4, ROTOR_REVERSE_CONVERSION5]

        self.reflectorConversion = REFLECTOR_CONVERSION

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
        return (self.rotorConversion[rotor_num - 1][(char_input_num + rotor_index - ring_setting) % 26] - rotor_index + ring_setting) % 26

    def letter_index_reverse_conversions(self, char_input, rotor_num, rotor_index, ring_setting):
        return (self.rotorReverseConversion[rotor_num - 1][(char_input + rotor_index - ring_setting) % 26] - rotor_index + ring_setting) % 26

    def circular_shift(self):
        if self.firstRotorIndex == self.firstTurnoverNotch - 1 or self.secondRotorIndex == self.secondTurnoverNotch - 1:
            if self.secondRotorIndex == self.secondTurnoverNotch - 1:
                self.thirdRotorIndex = (self.thirdRotorIndex + 1) % 26
            self.secondRotorIndex = (self.secondRotorIndex + 1) % 26
        self.firstRotorIndex = (self.firstRotorIndex + 1) % 26

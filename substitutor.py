from consts import ROTOR_CONVERSION, ROTOR_REVERSE_CONVERSION,REFLECTOR_CONVERSION

class Substitutor():
    def __init__(self):
        self.configured = False
        self.firstTurnoverNotch = 0
        self.secondTurnoverNotch = 0
        self.thirdTurnoverNotch = 0

        self.firstRotorIndex = 0
        self.secondRotorIndex = 0
        self.thirdRotorIndex = 0

        self.rotorConversion = ROTOR_CONVERSION

        self.rotorReverseConversion = ROTOR_REVERSE_CONVERSION

        self.reflectorConversion = REFLECTOR_CONVERSION

    def set_rotor_order(self, first, second, third):
        if first == 1:
            self.firstTurnoverNotch = 16
        elif first == 2:
            self.firstTurnoverNotch = 4
        elif first == 3:
            self.firstTurnoverNotch = 21
        elif first == 4:
            self.firstTurnoverNotch = 9
        elif first == 5:
            self.firstTurnoverNotch = 25

        if second == 1:
            self.secondTurnoverNotch = 16
        elif second == 2:
            self.secondTurnoverNotch = 4
        elif second == 3:
            self.secondTurnoverNotch = 21
        elif second == 4:
            self.secondTurnoverNotch = 9
        elif second == 5:
            self.secondTurnoverNotch = 25

        if third == 1:
            self.thirdTurnoverNotch = 16
        elif third == 2:
            self.thirdTurnoverNotch = 4
        elif third == 3:
            self.thirdTurnoverNotch = 21
        elif third == 4:
            self.thirdTurnoverNotch = 9
        elif third == 5:
            self.thirdTurnoverNotch = 25

    def letter_index_conversions(self, char_input_num, rotor_num, rotor_index, ring_setting):
        return (self.rotorConversion[rotor_num - 1][(char_input_num + rotor_index - ring_setting) % 26] - rotor_index + ring_setting) % 26

    def letter_index_reverse_conversions(self, char_input, rotor_num, rotor_index, ring_setting):
        return (self.rotorReverseConversion[rotor_num - 1][(char_input + rotor_index - ring_setting) % 26] - rotor_index + ring_setting) % 26

    def circular_shift(self):
        if self.firstRotorIndex == self.firstTurnoverNotch or self.secondRotorIndex == self.secondTurnoverNotch:
            if self.secondRotorIndex == self.secondTurnoverNotch:
                self.thirdRotorIndex = (self.thirdRotorIndex + 1) % 26
            self.secondRotorIndex = (self.secondRotorIndex + 1) % 26
        self.firstRotorIndex = (self.firstRotorIndex + 1) % 26
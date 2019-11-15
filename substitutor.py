from consts import ROTOR_CONVERSION, ROTOR_REVERSE_CONVERSION, REFLECTOR_CONVERSION
'''
Substitutor contains all rotors permutation array(forward and reverse), reflector permutation array.
Substitutor Responsible for permutation result and rotors rotate.
'''
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
    '''
    sets the rotors TurnoverNotch according the 3 selected rotors (out of 5)
    '''
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
    '''
    Performing the Forward permutation according to next formula:
    For an input letter A, ring offset B, ring setting C, and rotor forward or
    reverse permutation P, the result is given by P(A+B−C)−B+C.
    when P = rotorConversion array according to chosen rotor.
    '''
    def letter_index_conversions(self, char_input_num, rotor_num, ring_offset, ring_setting):
        return (self.rotorConversion[rotor_num][
                    (char_input_num + ring_offset - ring_setting) % 26] - ring_offset + ring_setting) % 26

    '''
        Performing the Reverse permutation according to next formula:
        For an input letter A, ring offset B, ring setting C, and rotor forward or
        reverse permutation P, the result is given by P(A+B−C)−B+C.
        when P = rotorReverseConversion array according to chosen rotor.
        '''
    def letter_index_reverse_conversions(self, char_input, rotor_num, ring_offset, ring_setting):
        return (self.rotorReverseConversion[rotor_num][
                    (char_input + ring_offset - ring_setting) % 26] - ring_offset + ring_setting) % 26
    '''
    Each key press steps at least one rotor before translation is per-formed. For left, middle and right rotors (L, M, R),
    the stepping algorithm is as follows:
    if R.notch or M.notch
        if M.notch
            advance L.offset
        advance M.offset
    advance R.offset
    '''
    def circular_shift(self):
        if self.firstRotorIndex == self.firstTurnoverNotch or self.secondRotorIndex == self.secondTurnoverNotch:
            if self.secondRotorIndex == self.secondTurnoverNotch:
                self.thirdRotorIndex = (self.thirdRotorIndex + 1) % 26
            self.secondRotorIndex = (self.secondRotorIndex + 1) % 26
        self.firstRotorIndex = (self.firstRotorIndex + 1) % 26

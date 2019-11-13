from substitutor import Substitutor
from consts import LETTER_A_IN_ASCII

class Enigma(Substitutor):
    s_first = 0
    s_second = 0
    s_third = 0

    s_FirstRingSetting = 0
    s_SecondRingSetting = 0
    s_ThirdRingSetting = 0

    s_firstRotorIndex = 0
    s_secondRotorIndex = 0
    s_thirdRotorIndex = 0

    def machine_configuration_process(self, first, first_key, first_ring_setting, second, second_key,
                                      second_ring_setting, third, third_key, third_ring_setting, plug_board):
        s_first = first - 1
        s_second = second - 1
        s_third = third - 1
        self.set_rotor_order(first, second, third)
        s_FirstRingSetting = first_ring_setting
        s_SecondRingSetting = second_ring_setting
        s_ThirdRingSetting = third_ring_setting

        s_firstRotorIndex = first_key
        s_secondRotorIndex = second_key
        s_thirdRotorIndex = third_key

        self.plugBoard = plug_board
        self.configured = True

    def complete_text_translation(self, text):
        for c in text:
            c = self.plugBoard.plugs[c]
            c_to_num = ord(c) - LETTER_A_IN_ASCII

            self.circular_shift()
            encrypt_process = self.letter_index_conversions(c_to_num, Enigma.s_first,
                                                                   Enigma.s_firstRotorIndex, Enigma.s_FirstRingSetting)
            encrypt_process = self.letter_index_conversions(encrypt_process, Enigma.s_second,
                                                                   Enigma.s_secondRotorIndex, Enigma.s_SecondRingSetting)
            encrypt_process = self.letter_index_conversions(encrypt_process, Enigma.s_third,
                                                                   Enigma.s_thirdRotorIndex, Enigma.s_ThirdRingSetting)
            encrypt_process = self.reflectorConversion[encrypt_process]
            encrypt_process = self.letter_index_reverse_conversions(encrypt_process, Enigma.s_third,
                                                                           Enigma.s_thirdRotorIndex, Enigma.s_ThirdRingSetting)
            encrypt_process = self.letter_index_reverse_conversions(encrypt_process, Enigma.s_second,
                                                                           Enigma.s_secondRotorIndex, Enigma.s_SecondRingSetting)
            encrypt_process = self.letter_index_reverse_conversions(encrypt_process, Enigma.s_first,
                                                                           Enigma.s_firstRotorIndex, Enigma.s_FirstRingSetting)
            encrypt_process = self.plugBoard.plugs[chr(encrypt_process+65)]

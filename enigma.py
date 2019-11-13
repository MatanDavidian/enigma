from substitutor import Substitutor
from consts import LETTER_A_IN_ASCII

class Enigma(Substitutor):

    def machine_configuration_process(self, first, first_key, first_ring_setting, second, second_key,
                                      second_ring_setting, third, third_key, third_ring_setting, plug_board):
        self.first = first
        self.second = second
        self.third = third
        self.set_rotor_order(first, second, third)
        self.FirstRingSetting = first_ring_setting
        self.SecondRingSetting = second_ring_setting
        self.ThirdRingSetting = third_ring_setting
        self.firstRotorIndex = first_key
        self.secondRotorIndex = second_key
        self.thirdRotorIndex = third_key
        self.plugBoard = plug_board
        self.configured = True

    def complete_text_translation(self, text):
        for c in text:
            c = self.plugBoard.plugs[c]
            # the ASCII value of the char
            c_to_num = ord(c) - LETTER_A_IN_ASCII

            Substitutor.circular_shift(self)
            encrypt_process = self.letter_index_conversions(c_to_num, self.first,
                                                                   self.firstRotorIndex, self.FirstRingSetting)
            encrypt_process = self.letter_index_conversions(encrypt_process, self.second,
                                                                   self.secondRotorIndex, self.SecondRingSetting)
            encrypt_process = self.letter_index_conversions(encrypt_process, self.third,
                                                                   self.thirdRotorIndex, self.ThirdRingSetting)
            encrypt_process = self.reflectorConversion[encrypt_process]
            encrypt_process = self.letter_index_reverse_conversions(encrypt_process, self.third,
                                                                           self.thirdRotorIndex, self.ThirdRingSetting)
            encrypt_process = self.letter_index_reverse_conversions(encrypt_process, self.second,
                                                                           self.secondRotorIndex, self.SecondRingSetting)
            encrypt_process = self.letter_index_reverse_conversions(encrypt_process, self.first,
                                                                           self.firstRotorIndex, self.FirstRingSetting)
            encrypt_process = self.plugBoard.plugs[chr(encrypt_process+65)]
            # print(encrypt_process, end='')


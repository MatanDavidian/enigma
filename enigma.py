from substitutor import Substitutor


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
        if self.configured:
            for c in text:
                if 'A' <= c <= 'Z':
                    c = self.plugBoard.plugs[c]
                    # the ASCII value of the char
                    c_to_num = ord(c) - 65

                    Substitutor.circular_shift(self)
                    encrypt_process = Substitutor.letter_index_conversions(self, c_to_num, self.first,
                                                                           self.firstRotorIndex, self.FirstRingSetting)
                    encrypt_process = Substitutor.letter_index_conversions(self, encrypt_process, self.second,
                                                                           self.secondRotorIndex, self.SecondRingSetting)
                    encrypt_process = Substitutor.letter_index_conversions(self, encrypt_process, self.third,
                                                                           self.thirdRotorIndex, self.ThirdRingSetting)
                    encrypt_process = self.reflectorConversion[encrypt_process]
                    encrypt_process = Substitutor.letter_index_reverse_conversions(self, encrypt_process, self.third,
                                                                                   self.thirdRotorIndex, self.ThirdRingSetting)
                    encrypt_process = Substitutor.letter_index_reverse_conversions(self, encrypt_process, self.second,
                                                                                   self.secondRotorIndex, self.SecondRingSetting)
                    encrypt_process = Substitutor.letter_index_reverse_conversions(self, encrypt_process, self.first,
                                                                                   self.firstRotorIndex, self.FirstRingSetting)
                    encrypt_process = self.plugBoard.plugs[chr(encrypt_process+65)]
                    print(encrypt_process, end='')
        else:
            print("enigma is not configured")

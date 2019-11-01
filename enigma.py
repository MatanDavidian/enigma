from substitutor import Substitutor


class Enigma(Substitutor):

    def machine_configuration_process(self, first, first_key, second, second_key, third, third_key):
        self.first = first
        self.second = second
        self.third = third
        self.set_rotor_order(first, second, third)
        self.firstRotorIndex = first_key
        self.secondRotorIndex = second_key
        self.thirdRotorIndex = third_key
        self.configured = True

    def complete_letter_translation(self, text):
        if self.configured == True:
            for c in text:
                if 'A' <= c <= 'Z':
                    c_to_num = ord(c) - 65

                    Substitutor.circular_shift(self)
                    encrypt_process = Substitutor.letter_index_conversions(self, c_to_num, self.first, self.firstRotorIndex)
                    #print(encrypt_process)
                    encrypt_process = Substitutor.letter_index_conversions(self, encrypt_process, self.second, self.secondRotorIndex)
                    #print(encrypt_process)
                    encrypt_process = Substitutor.letter_index_conversions(self, encrypt_process, self.third, self.thirdRotorIndex)
                    #print(encrypt_process)
                    encrypt_process = ord(self.reflectorConversion[encrypt_process]) - 65
                    #print(encrypt_process)
                    encrypt_process = Substitutor.letter_index_reverse_conversions(self, encrypt_process, self.third, self.thirdRotorIndex)
                    #print(encrypt_process)
                    encrypt_process = Substitutor.letter_index_reverse_conversions(self, encrypt_process, self.second, self.secondRotorIndex)
                    #print(encrypt_process)
                    encrypt_process = Substitutor.letter_index_reverse_conversions(self, encrypt_process, self.first, self.firstRotorIndex)
                    #print(encrypt_process)
                    encrypt_process = self.plugBoard[encrypt_process]
                    print(encrypt_process, end='')
        else:
            print("enigma is not configured")

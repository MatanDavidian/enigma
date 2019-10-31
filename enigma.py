from substitutor import Substitutor


class Enigma(Substitutor):
    num_of_rotors = 0
    def complete_letter_translation(self, text):

        for c in text:
            if 'A' <= c <= 'Z':
                c_to_num = ord(c) - 65

                Substitutor.circular_shift(self)
                encrypt_process = Substitutor.letter_index_conversions(self, c_to_num, 5)
                #print(encrypt_process)
                encrypt_process = Substitutor.letter_index_conversions(self, encrypt_process, 4)
                #print(encrypt_process)
                encrypt_process = Substitutor.letter_index_conversions(self, encrypt_process, 3)
                #print(encrypt_process)
                encrypt_process = ord(Substitutor.reflectorConversion[encrypt_process]) -65
                #print(encrypt_process)
                encrypt_process = Substitutor.letter_index_reverse_conversions(self, encrypt_process, 3)
                #print(encrypt_process)
                encrypt_process = Substitutor.letter_index_reverse_conversions(self, encrypt_process, 4)
                #print(encrypt_process)
                encrypt_process = Substitutor.letter_index_reverse_conversions(self, encrypt_process, 5)
                #print(encrypt_process)
                encrypt_process = Substitutor.plugBoard[encrypt_process]
            print(encrypt_process)


e = Enigma()
e.complete_letter_translation("ENIGMA")

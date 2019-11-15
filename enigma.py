from substitutor import Substitutor
from consts import LETTER_A_IN_ASCII
'''
The Enigma machine inherit from Substitutor all rotors and reflector, and contain plug board object
'''
class Enigma(Substitutor):
    '''
    configure the enigma machine for encrypt/decrypt.
    by set rotors order(1-5), rotors offset(0-25), rotor setting(0-25) and plug board (partial configurations : less than 10 pairs)
    '''
    def machine_configuration_process(self, first, first_key, first_ring_setting, second, second_key,
                                      second_ring_setting, third, third_key, third_ring_setting, plug_board):
        self.right = first - 1
        self.middle = second - 1
        self.left = third - 1
        self.set_rotor_order(first, second, third)

        self.right_rings_setting = first_ring_setting
        self.middle_ring_ssetting = second_ring_setting
        self.left_ring_setting = third_ring_setting

        self.firstRotorIndex = first_key
        self.secondRotorIndex = second_key
        self.thirdRotorIndex = third_key

        self.plugBoard = plug_board
        self.configured = True
    '''
    get a encrypt/decrypt text and according to machine configuration encrypt/decrypt the text, by
    Activate the following for each letter: 
    each letter is transformed through the plugboard,
    right rotor, middle rotor, left rotor, reflector, left rotor (reverse direction), middle rotor (re-
    verse direction), right rotor (reverse direction), and plugboard again. When a key is pressed,
    the rotors rotate before the translation.
    '''
    def complete_text_translation(self, text):
        for c in text:
            # rotors rotate
            self.circular_shift()
            # transformed through the plugboard
            c = self.plugBoard.plugs[c]
            c_to_num = ord(c) - LETTER_A_IN_ASCII

            # transformed through right rotor Forward permutation
            encrypt_process = self.letter_index_conversions(c_to_num, self.right,
                                                            self.firstRotorIndex, self.right_rings_setting)
            # transformed through middle rotor Forward permutation
            encrypt_process = self.letter_index_conversions(encrypt_process, self.middle,
                                                                   self.secondRotorIndex, self.middle_ring_ssetting)
            # transformed through left rotor Forward permutation
            encrypt_process = self.letter_index_conversions(encrypt_process, self.left,
                                                                   self.thirdRotorIndex, self.left_ring_setting)

            # transformed through the reflector
            encrypt_process = self.reflectorConversion[encrypt_process]

            # transformed through left rotor reverse direction
            encrypt_process = self.letter_index_reverse_conversions(encrypt_process, self.left,
                                                                           self.thirdRotorIndex, self.left_ring_setting)
            # transformed through middle rotor reverse direction
            encrypt_process = self.letter_index_reverse_conversions(encrypt_process, self.middle,
                                                                           self.secondRotorIndex, self.middle_ring_ssetting)
            # transformed through right rotor reverse direction
            encrypt_process = self.letter_index_reverse_conversions(encrypt_process, self.right,
                                                                           self.firstRotorIndex, self.right_rings_setting)

            # transformed through the plugboard again
            encrypt_process = self.plugBoard.plugs[chr(encrypt_process+65)]

            print(encrypt_process, end='')

from translator import Translator
from consts import LETTER_A_IN_ASCII,LETTER_Z_IN_ASCII
"""
    this class holds the dictionary which simulate the plugboard.
    with this class you can:
    -   create this dict.
    -   connect plugs to each other.
"""
class Plugboard():
    """
        Creates a dictionary called "plugs".
        In this dict. the keys and the values are both CHARS
        for easy switching, and using.
    """
    def __init__(self):
        self.plugs={}
        for i in range (LETTER_A_IN_ASCII,LETTER_A_IN_ASCII+1):
            self.plugs[chr(i)] = chr(i)
    """
        Connecting plug1 to plug2 , and plug2 to plug1
    """
    def connectPair(self, plug1, plug2):
        try:
            if self.plugs[plug1] == plug1 and self.plugs[plug2] == plug2:
                self.plugs[plug1], self.plugs[plug2] = plug2, plug1
            else:
                print("one of the letters already connected")
        except:
            print("please use single capital letters only")

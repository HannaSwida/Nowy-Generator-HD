from model import *

class Baza(object):
    def __init__(self):
        self.osoby = []
        self.komisariaty = []
        self.funkcjonariusze = []
        self.wystawione_mandaty = []
        self.aresztowania = []
    def dump(self, target_directory):

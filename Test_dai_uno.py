import os
import sys
import random
import math
import time

class BadInputError(Exception)
    pass

class Player():

    def __init__(self, name):
        self.id = None
        self.name = name
        self.type = 'Human'
        self.hand = Hand()
        self.legalCards = []
        self.wildCards = []
        self.valueChangeCards = []


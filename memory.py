
'''
Base class file for Memory (DRAM)
Credit: A. Jog (W&M), Ramulator (CMU)
'''

import numpy as np
from math import log2
import random


class Memory:
    def __init__(self, row_size=2048):
        self.Row_size = row_size
        self.open_row = -1
        self.rowBits = int(log2(self.Row_size))
        self.rowhitlatency = 100
        self.rowmisslatency = 200

    def get_open_row(self):
        return self.open_row

    def set_open_row(self, row_number):
        self.open_row = row_number

    def find_row_number(self, address):
        return (address >> self.rowBits)

    def is_row_hit(self, address):
        return (self.find_row_number(address) == self.get_open_row())

    '''
    Warning: DO NOT EDIT Anything Above
    '''

    def determine_miss_penalty(self, address):
        # First, check if the requested address matches the currently active row in the row buffer.
        if self.is_row_hit(address):
            # If it's a hit, we already have the row loaded - send back the hit latency.
            return self.rowhitlatency

        else:
            # If it's a miss, we need to load a new row into the row buffer.
            self.set_open_row(self.find_row_number(address))
            return self.rowmisslatency

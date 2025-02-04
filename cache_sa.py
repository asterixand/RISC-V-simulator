
# Write team member names here: Rithani Priyanga Coimbatore Kannan


'''
Base class file for building a set-associative cache
Credit: R. Martin (W&M), A. Jog (W&M), Ramulator (CMU)
'''

import numpy as np
from math import log
import random


class Cache:
    def __init__(self, cSize, ways=2, bSize=4):
        '''
        Keep ways > 1 to keep the cache set associative
        '''

        if ways < 1:
            print("Invalid configuration: Ways must be >= 1")
            exit(0)

        if ways == 1:
            print("Initializing Direct-Mapped Cache")
        else:
            print("Initializing Set-Associative Cache")

        self.cacheSize = cSize  # Bytes
        self.ways = ways        # Default: 2 way (i.e., set associative)
        self.blockSize = bSize  # Default: 4 bytes (i.e., 1 word block)
        self.sets = cSize // bSize // ways

        self.blockBits = 0
        self.setBits = 0

        if (self.blockSize != 1):
            self.blockBits = int(log(self.blockSize, 2))

        if (self.sets != 1):
            self.setBits = int(log(self.sets, 2))

        self.cache = np.zeros(
            (self.sets, self.ways, self.blockSize), dtype=int)
        self.cache = self.cache - 1

        self.metaCache = np.zeros((self.sets, self.ways), dtype=np.int64) - 1

        self.hit = 0
        self.miss = 0
        self.hitlatency = 1  # cycle
        self.misspenalty = 10  # cycle
        self.lru_order = [[] for _ in range(self.sets)]

    def reset(self):
        self.cache = np.zeros(
            (self.sets, self.ways, self.blockSize), dtype=int) - 1

        # IMPORTANT EDIT: dtype=np.int64: using 64-bit integers because tags can be large numbers
        self.metaCache = np.zeros((self.sets, self.ways), dtype=np.int64) - 1
        self.hit = 0
        self.miss = 0
        self.lru_order = [[] for _ in range(self.sets)]

    '''
    Warning: DO NOT EDIT ANYTHING ABOVE THIS LINE
    '''

    '''
    Returns the set number of an address based on the policy discussed in the class
    Do NOT change the function definition and arguments
    '''

    def find_set(self, address):
        # Shifting right by blockBits to ignore block offset bits
        # Applying modulo by sets to get a valid set index within the range
        return (address >> self.blockBits) % self.sets

    '''
    Returns the tag of an address based on the policy discussed in the class
    Do NOT change the function definition and arguments
    '''

    def find_tag(self, address):
        # Shifting right by setBits + blockBits to ignore both set and block bits, leaving only the tag bits
        return address >> (self.setBits + self.blockBits)

    '''
    Search through cache for address
    return True if found
    otherwise False
    Do NOT change the function definition and arguments
    '''

    def find(self, address):
        if self.ways == 1:  # Direct-mapped cache
            set_index = self.find_set(address)
            tag = self.find_tag(address)

            if self.metaCache[set_index][0] == tag:
                self.hit += 1
                return True
            return False
        else:
            set_index = self.find_set(address)
            tag = self.find_tag(address)

            # Check if tag exists in the set
            for way in range(self.ways):
                if self.metaCache[set_index][way] == tag:
                    # Only increment hit if we actually found the tag
                    self.hit += 1
                    # Update LRU order
                    way_index = self.lru_order[set_index].index(way)
                    self.lru_order[set_index].pop(way_index)
                    self.lru_order[set_index].append(way)
                    return True
            return False
    '''
    Load data into the cache. 
    Something might need to be evicted from the cache and send back to memory
    Do NOT change the function definition and arguments
    '''

    def load(self, address):
        if self.ways == 1:  # Direct-mapped cache
            set_index = self.find_set(address)
            tag = self.find_tag(address)
            self.metaCache[set_index][0] = tag
            return
        else:
            set_index = self.find_set(address)
            tag = self.find_tag(address)

            # Checking if there's an empty way to place the new data
            for way in range(self.ways):
                # -1 means empty
                if self.metaCache[set_index][way] == -1:
                    # Store the tag in the empty way
                    self.metaCache[set_index][way] = tag
                    # Update LRU order with this way as most recent
                    self.lru_order[set_index].append(way)
                    return

            # Ignoring the least recently used way (first in LRU order)
            # Remove LRU way from the order
            lru_way = self.lru_order[set_index].pop(0)
            # Place new tag
            self.metaCache[set_index][lru_way] = tag
            # Update LRU order with this way as most recent
            self.lru_order[set_index].append(lru_way)

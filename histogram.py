import sys
import re
from datetime import datetime
from operator import itemgetter

class Histogram(list):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new list; update with given items"""
        super(Histogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        # go through every item in the list to be added
        # each one is a new token
        for item in iterable:
            self.add(item)

    def add(self, item):
        # increment the number of tokens
        self.tokens += 1
        self.increment_frequency(item)

    def increment_frequency(self, word, count=1):
        found = False
        for index, tup in enumerate(self):
            if tup[0] == word:
                current = tup[1]
                self[index] = (word, current + count)
                found = True
        if not found:
            self.append((word, 1))
            self.types += 1


    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        for tup in self:
            if tup[0] == item:
                return tup[1]
        return 0

    def __contains__(self, item):
        """Return True if the given item is in this histogram, or False"""
        for tup in self:
            if tup[0] == item:
                return True
        return False

    def _index(self, target):
        """Return the index of the (target, count) entry if found, or None"""
        for index, item in enumerate(self):
            if item == target:
                return index

if __name__ == '__main__':
    # calculate time to create a histogram
    start = datetime.now()
    test_hist = Histogram('blue.txt')
    print("Time: " + str(datetime.now() - start))

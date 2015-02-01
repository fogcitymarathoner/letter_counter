__author__ = 'marc'
"""
LetterCounter Class - Tracks a list of Letter Classes
 members
   letters - list of letters
   is_counting() - is letter actively being counted
   append() - add letter class with count of one
   increment() - increment count on active letter
"""
class Letter:
    letter = ''
    count = 0
    def __init__(self, letter):
        self.letter = letter
        self.count = 1

class LetterCounter:
    letters = []
    def __init__(self, letter):
        letter = Letter(letter)
        self.letters.append(letter)

    def is_counting(self, letter):
        pass
    def append(self, letter):
        pass
    def increment(self, letter):
        pass
__author__ = 'marc'
import unittest
from lib.letter_counter import LetterCounter
from lib.letter_counter import Letter
class LetterCounterAppendTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_append(self):
        """
        test_append - make sure new non controlled letters append right onto LetterCounter.letters list
        """

        lc = LetterCounter('a')

        lc.append('b')

        self.assertEqual(2, len(lc.letters))
        self.assertEqual(1, lc.letters[1].count)

    def test_append_twice(self):

        lc = LetterCounter('a')

        lc.append('b')
        lc.append('b')

        self.assertEqual(2, len(lc.letters))
        self.assertEqual(1, lc.letters[1].count)
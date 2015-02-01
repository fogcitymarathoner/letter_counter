__author__ = 'marc'
import unittest
from lib.letter_counter import LetterCounter
from lib.letter_counter import Letter
class LetterCounterAppendTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_increment(self):
        """
        test_increment - make sure letter undercontrol count increments
        """

        lc = LetterCounter('a')

        lc.append('b')

        self.assertEqual(2, len(lc.letters))
        self.assertEqual(1, lc.letters[1].count)
        lc.increment('b')
        self.assertEqual(2, lc.letters[1].count)

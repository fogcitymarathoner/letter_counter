__author__ = 'marc'
import unittest
from lib.letter_counter import LetterCounter
class LetterCounterInitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        """
        test_init - makes sure letter counter initializes right
        """

        lc = LetterCounter('a')
        self.assertEqual('a', lc.letters[0].letter)
        self.assertEqual(1, lc.letters[0].count)

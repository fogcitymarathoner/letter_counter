__author__ = 'marc'
import unittest
from lib.letter_counter import LetterCounter
class LetterCounterIsCountingTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        """
        test_init - makes sure letter counter initializes right
        """

        lc = LetterCounter('a')
        

        self.assertTrue(lc.is_counting('a'))
        self.assertFalse(lc.is_counting('b'))

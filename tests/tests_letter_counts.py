__author__ = 'marc'
import unittest
from lib.letter_counter import LetterCounter
from lib.letter_counter import Letter
from lib.functions import letter_counts
class LetterCountsTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_increment(self):
        """
        test_increment - make sure letter undercontrol count increments
        """

        letters = letter_counts('Hello World!')
        self.assertEqual('H', letters[0].letter)
        self.assertEqual(1, letters[0].count)
        self.assertEqual('e', letters[1].letter)
        self.assertEqual(1, letters[1].count)
        self.assertEqual('l', letters[2].letter)
        self.assertEqual(3, letters[2].count)
        self.assertEqual('o', letters[3].letter)
        self.assertEqual(2, letters[3].count)
        self.assertEqual(' ', letters[4].letter)
        self.assertEqual(1, letters[4].count)
        self.assertEqual('W', letters[5].letter)
        self.assertEqual(1, letters[5].count)
        self.assertEqual('r', letters[6].letter)
        self.assertEqual(1, letters[6].count)
        self.assertEqual('d', letters[7].letter)
        self.assertEqual(1, letters[7].count)
        self.assertEqual('!', letters[8].letter)
        self.assertEqual(1, letters[8].count)

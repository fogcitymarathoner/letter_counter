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

    def test_increment_letter_not_under_control(self):
        """
        test_increment_letter_not_under_control - make sure incrementing letter not under control doesn't affect letters
        list
        :return:
        """

        lc = LetterCounter('a')

        lc.append('b')

        self.assertEqual(2, len(lc.letters))
        self.assertEqual(1, lc.letters[1].count)
        lc.increment('b')
        self.assertEqual(2, lc.letters[1].count)
        lc.increment('z')
        self.assertEqual(2, len(lc.letters))
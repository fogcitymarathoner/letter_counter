__author__ = 'marc'
import unittest
from lib.letter_counter import LetterCounter
from lib.letter_counter import Letter
class LetterUrlencodeTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_urlencode(self):
        """
        test_urlencode - make sure template can do a lazy urlencode, keeping template cleaner
        """

        lc = Letter(' ')
        self.assertEqual('%20', lc.urlencode())
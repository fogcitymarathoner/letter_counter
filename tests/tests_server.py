__author__ = 'marc'
import unittest
import requests
from bs4 import BeautifulSoup as bs
class ServerTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_server(self):
        """
        test_server - make sure html server works
        """

        r = requests.get('https://fogtest.com/letter_counter/', verify=False)

        doc = bs(r.text)
        self.assertEqual('Letter Counter', doc.find('title').text)
        
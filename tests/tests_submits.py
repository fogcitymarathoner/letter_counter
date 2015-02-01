__author__ = 'marc'
import unittest
import requests
from bs4 import BeautifulSoup as bs
class SubmitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_submit(self):
        """
        test_get_submit - make sure q=fred returns right result
        """

        r = requests.get('https://fogtest.com/letter_counter/?q=fred', verify=False)

        doc = bs(r.text)
        self.assertEqual('fred', doc.find('input', {'id': 'q'}).get('value'))


    def test_post_submit(self):
        """
        test_post_submit - make sure intended POST request returns right result
        :return:
        """
        data = {
            'q': 'fred',
        }

        r = requests.post('https://fogtest.com/letter_counter/', data=data, verify=False)

        doc = bs(r.text)
        self.assertEqual('fred', doc.find('input', {'id': 'q'}).get('value'))


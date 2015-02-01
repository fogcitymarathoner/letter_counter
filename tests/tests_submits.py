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
        self.assertEqual('fred', doc.find('textarea', {'id': 'q'}).get('value'))

    def test_get_submit_carriagereturn(self):
        """
        test_get_submit_carriagereturn - make sure q=fred returns right result
        """

        r = requests.get('https://fogtest.com/letter_counter/?q=fr%0d:ed', verify=False)

        doc = bs(r.text)
        self.assertEqual('fr\r:ed', doc.find('textarea', {'id': 'q'}).get('value'))

    def test_get_submit_null(self):
        """
        test_get_submit_null - make sure q= where null returns right result
        """

        r = requests.get('https://fogtest.com/letter_counter/?q=', verify=False)

        doc = bs(r.text)
        self.assertEqual('', doc.find('textarea', {'id': 'q'}).get('value'))


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

        td_qstrs = doc.find_all('td', {'class': 'qstr'})

        self.assertEqual('\'f\'', td_qstrs[0].text)
        self.assertEqual('\'r\'', td_qstrs[1].text)
        self.assertEqual('\'e\'', td_qstrs[2].text)
        self.assertEqual('\'d\'', td_qstrs[3].text)


        td_counts = doc.find_all('td', {'class': 'count'})
        self.assertEqual('1', td_counts[0].text)
        self.assertEqual('1', td_counts[1].text)
        self.assertEqual('1', td_counts[2].text)
        self.assertEqual('1', td_counts[3].text)
    def xtest_post_submit_null(self):
        """
        test_post_submit_null - make sure intended POST request returns right result with null input
        :return:
        """
        data = {
            'q': None,
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'
        }
        r = requests.post('https://fogtest.com/letter_counter/', data=data, verify=False, headers=headers)
        print r.text
        doc = bs(r.text)
        self.assertEqual('fred', doc.find('input', {'id': 'q'}).get('value'))


    def xtest_post_submit_carriagereturn(self):
        """
        test_post_submit_null - make sure intended POST request returns right result with null input
        :return:
        """
        data = {
            'q': None,
        }

        r = requests.post('https://fogtest.com/letter_counter/', data=data, verify=False)
        print r.text
        doc = bs(r.text)
        self.assertEqual('fr%0d:ed', doc.find('input', {'id': 'q'}).get('value'))

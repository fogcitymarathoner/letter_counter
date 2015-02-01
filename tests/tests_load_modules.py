__author__ = 'marc'
import unittest

class LetterModuleImportTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_imports(self):
        """
        test_imports - makes sure modules will load
        """
        module_list = [
            'lib',
            'lib.letter_counter',
            'lib.functions',
            ]
        for mod in module_list:
            try:
                __import__(mod)

            except ImportError:
                print mod
                self.assertTrue(False)
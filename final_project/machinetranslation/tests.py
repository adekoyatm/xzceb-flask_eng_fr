import unittest

from machinetranslation.translator import french_to_english, english_to_french

class Testfrench_to_english(unittest.TestCase):
    def test1(self):
        self.assertIsNotNone(french_to_english("Bonjour"))
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

class Testenglish_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertIsNotNone(english_to_french('Hello'))

unittest.main()

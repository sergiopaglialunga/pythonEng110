import unittest

from scrabble_dicc import scrable, string1

class Test(unittest.TestCase):

    result = ScrableScore()

    def test_score(self):
        self.assertEqual(self.result(string1), 144)

    # def test_add(self):
    #     self.assertEqual(self.calc.add(2, 4), 6)
    #
    # def test_subtract(self):
    #     self.assertEqual(self.calc.subtract(4, 2), 2)
    #
    # def test_multiply(self):
    #     self.assertEqual(self.calc.multiply(2, 4), 8)
    #
    # def test_divide(self):
    #     self.assertEqual(self.calc.divide(8, 4), 2)
import unittest

from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_initialValue(self):
        self.assertEqual(self.calc.value, 0)

    def test_add_method(self):
        self.calc.add(2, 3)
        self.assertEqual(self.calc.value, 5)

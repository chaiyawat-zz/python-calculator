import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add1(self):
        self.assertEqual(self.calc.add(6, 7), 13)

    def test_add2(self):
        self.assertEqual(self.calc.add(0, 7), 7)

    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(7, 10), -3)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(3, 1000), 3000)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(6, 2), 3)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)

    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(9, 2), 1)
   

if __name__ == '__main__':
    unittest.main()
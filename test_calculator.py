import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.subtract(4,2),2)
    def test_add_negative2(self):
        self.assertEqual(self.calc.subtract(4,-2),6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,3),6)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(2,-3),-6)
    def test_multiply3(self):
        self.assertEqual(self.calc.multiply(0,3),0)

    def test_divi(self):
        self.assertEqual(self.calc.divide(10,2),5)
    def test_divi2(self):
        self.assertEqual(self.calc.divide(10,-2),-5)


    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10,3),1)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(10,0),"Undefined")

if __name__ == '__main__':
    unittest.main()
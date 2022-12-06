import unittest
import gg as testing_app


class CalculatorAppTests(unittest.TestCase):
    def setUp(self):
        self.calculator = testing_app

    def test_add(self):
        self.assertEqual(self.calculator.calulator("1 + 9 + 5"), 15)

    def test_subtract(self):
        self.assertEqual(self.calculator.calulator("50 - 5 - 5 - 25"), 15)

    def test_multiply(self):
        self.assertEqual(self.calculator.calulator("7 * 1 * 3"), 21)

    def test_divide(self):
        self.assertEqual(self.calculator.calulator("10 / 1 / 2"), 5)

    def test_all(self):
        self.assertEqual(self.calculator.calulator("1 + 2 * 3 - 9"), -2)


if __name__ == "__main__":
    unittest.main()
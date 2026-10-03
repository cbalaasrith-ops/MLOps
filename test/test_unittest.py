import unittest
from src.calculator import fun1, fun2, fun3, fun4


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(fun1(5, 3), 8)

    def test_fun2(self):
        self.assertEqual(fun2(5, 3), 2)

    def test_fun3(self):
        self.assertEqual(fun3(5, 3), 15)

    def test_fun4(self):
        self.assertEqual(fun4(5, 3), 25)


if __name__ == "__main__":
    unittest.main()
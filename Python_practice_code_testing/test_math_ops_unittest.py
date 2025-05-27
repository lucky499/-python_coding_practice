import unittest

from math_operations import adding_numbers, subtracting

class testMathOperations(unittest.TestCase):
    def test_adding_numbers(self) ->  None:
        self.assertEqual(adding_numbers(10, 5), 15)
        self.assertEqual(adding_numbers(-2, 2), 0)
        self.assertEqual(adding_numbers(0, 0), 0)
        self.assertEqual(adding_numbers(-2, -3), -5)

    def test_subtracting(self) -> None:
        self.assertEqual(subtracting(10, 5), 5)
        self.assertEqual(subtracting(-10, 5), -15)
        self.assertEqual(subtracting(-10, -5), -5)
        self.assertEqual(subtracting(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
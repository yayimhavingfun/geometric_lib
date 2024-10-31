import unittest
from calculate import calc


class CalcTestCase(unittest.TestCase):
    def test_valid_circle_area(self):
        result = calc('circle', 'area', [5])  # circle area with radius = 5
        self.assertAlmostEqual(result, 78.54, places=2)  # expected value with pi=3.1416

    def test_valid_square_perimeter(self):
        result = calc('square', 'perimeter', [4]) # square perimeter with a = 4
        self.assertEqual(result, 16) # expected result 4 * 4

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            calc('rectangle', 'area', [5, 10])  # unsupported figure "rectangle"

    def test_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc('circle', 'volume', [5])  # unsupported function "volume"

    def test_invalid_size_argument(self):
        with self.assertRaises(TypeError):
            calc('circle', 'area', ['not_a_number'])  # incorrect size argument type

    def test_invalid_size_length(self):
        with self.assertRaises(TypeError):
            calc('triangle', 'area', [5])  # not enough arguments for triangle function


if __name__ == '__main__':
    unittest.main()

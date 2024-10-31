import unittest
from calculate import calc


class CalcTestCase(unittest.TestCase):
    def test_valid_circle_area(self):
        # circle area with radius = 5
        result = calc('circle', 'area', [5])
        # expected value with pi=3.1416
        self.assertAlmostEqual(result, 78.54, places=2)

    def test_valid_square_perimeter(self):
        # square perimeter with a = 4
        result = calc('square', 'perimeter', [4])
        # expected result 4 * 4
        self.assertEqual(result, 16)

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            # unsupported figure "rectangle"
            calc('rectangle', 'area', [5, 10])

    def test_invalid_function(self):
        with self.assertRaises(AssertionError):
            # unsupported function "volume"
            calc('circle', 'volume', [5])

    def test_invalid_size_argument(self):
        with self.assertRaises(TypeError):
            # incorrect size argument type
            calc('circle', 'area', ['not_a_number'])

    def test_invalid_size_length(self):
        with self.assertRaises(TypeError):
            # not enough arguments for triangle function
            calc('triangle', 'area', [5])


if __name__ == '__main__':
    unittest.main()

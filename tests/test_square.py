import unittest
from square import area
from square import perimeter


class SquareTestCase(unittest.TestCase):
    # area tests
    def test_square_area_int(self):
        result = area(6)
        self.assertEqual(result, 36)

    def test_square_area_float(self):
        result = area(5.5)
        self.assertEqual(result, 30.25)

    def test_square_area_zero(self):
        result = area(0)
        self.assertEqual(result, "a cannot be 0")

    # perimeter tests
    def test_square_perimeter_int(self):
        result = perimeter(5)
        self.assertEqual(result, 20)

    def test_square_perimeter_float(self):
        result = perimeter(10.5)
        self.assertEqual(result, 42)

    def test_square_perimeter_zero(self):
        result = perimeter(0)
        self.assertEqual(result, "a cannot be 0")


if __name__ == '__main__':
    unittest.main()

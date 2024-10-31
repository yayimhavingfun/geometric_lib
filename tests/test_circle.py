import unittest
from circle import area
from circle import perimeter


class CircleTestCase(unittest.TestCase):
    # area tests
    def test_circle_area_int(self):
        result = area(4)
        self.assertEqual(result, 50.26548245743669)

    def test_circle_area_float(self):
        result = area(3.3)
        self.assertEqual(result, 34.21194399759285)

    def test_circle_area_zero(self):
        result = area(0)
        self.assertEqual(result, "r cannot be 0")

    # perimeter tests
    def test_circle_perimeter_int(self):
        result = perimeter(10)
        self.assertEqual(result, 62.83185307179586)

    def test_circle_perimeter_float(self):
        result = perimeter(5.5)
        self.assertEqual(result, 34.55751918948772)

    def test_circle_perimeter_zero(self):
        result = perimeter(0)
        self.assertEqual(result, "r cannot be 0")


if __name__ == '__main__':
    unittest.main()

import unittest
from triangle import area
from triangle import perimeter


class TriangleTestCase(unittest.TestCase):
    # area tests
    def test_triangle_area_int(self):
        result = area(2, 3, 4)
        self.assertEqual(result, 2.90474)

    def test_triangle_area_float(self):
        result = area(2.2, 3.3, 4.4)
        self.assertEqual(result, 3.5147)

    def test_triangle_area_mixed(self):
        result = area(3.3, 4, 5.5)
        self.assertEqual(result, 6.583)

    def test_triangle_area_zero(self):
        result = area(0, 0, 0)
        self.assertEqual(result, "values cannot be 0")

    def test_triangle_area_zero_mixed(self):
        result = area(0, 3, 0)
        self.assertEqual(result, "values cannot be 0")

    # perimeter area
    def test_triangle_perimeter_int(self):
        result = perimeter(2, 3, 4)
        self.assertEqual(result, 9)

    def test_triangle_perimeter_float(self):
        result = perimeter(2.2, 3.3, 4.4)
        self.assertEqual(result, 9.9)

    def test_triangle_perimeter_mixed(self):
        result = perimeter(3.3, 4, 5.5)
        self.assertEqual(result, 12.8)

    def test_triangle_perimeter_zero(self):
        result = perimeter(0, 0, 0)
        self.assertEqual(result, "values cannot be 0")

    def test_triangle_perimeter_zero_mixed(self):
        result = perimeter(0, 3, 0)
        self.assertEqual(result, "values cannot be 0")

    # validity tests
    def test_value_validity_c(self):
        result1 = area(1, 2, 3)
        result2 = perimeter(1, 2, 3)
        self.assertEqual(result1, result2)
        # should return "side c should be less than
        # the sum of the other two sides."

    def test_value_validity_b(self):
        result1 = area(1, 3, 2)
        result2 = perimeter(1, 3, 2)
        self.assertEqual(result1, result2)
        # should return "side b should be less than
        # the sum of the other two sides."

    def test_value_validity_a(self):
        result1 = area(3, 2, 1)
        result2 = perimeter(3, 2, 1)
        self.assertEqual(result1, result2)
        # should return "side a should be less than
        # the sum of the other two sides."


if __name__ == '__main__':
    unittest.main()

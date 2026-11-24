import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_zero_area(self):
        self.assertEqual(area(10, 0), 0)

    def test_square_area(self):
        self.assertEqual(area(10, 10), 100)

    def test_rectangle_area(self):
        self.assertEqual(area(5, 4), 20)

    def test_zero_perimeter(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_square_perimeter(self):
        self.assertEqual(perimeter(10, 10), 40)

    def test_rectangle_perimeter(self):
        self.assertEqual(perimeter(5, 4), 18)


if __name__ == '__main__':
    unittest.main()
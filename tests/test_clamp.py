import unittest

from calc import clamp


class ClampTests(unittest.TestCase):
    def test_value_inside_range(self):
        self.assertEqual(clamp(5, 1, 10), 5)

    def test_value_below_range(self):
        self.assertEqual(clamp(-3, 0, 10), 0)

    def test_value_above_range(self):
        self.assertEqual(clamp(42, 0, 10), 10)

    def test_low_greater_than_high(self):
        with self.assertRaises(ValueError) as error:
            clamp(5, 10, 1)
        self.assertEqual(str(error.exception), "low cannot be greater than high")


if __name__ == '__main__':
    unittest.main()

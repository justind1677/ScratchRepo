import unittest

from calc import add, percent_change


class AddTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)


class PercentChangeTests(unittest.TestCase):
    def test_increase(self):
        self.assertEqual(percent_change(100, 150), 50.0)

    def test_decrease(self):
        self.assertEqual(percent_change(80, 60), -25.0)

    def test_rounds_to_two_decimals(self):
        self.assertEqual(percent_change(3, 4), 33.33)

    def test_zero_old_value(self):
        with self.assertRaises(ValueError) as error:
            percent_change(0, 150)
        self.assertEqual(str(error.exception), "old value cannot be zero")


if __name__ == '__main__':
    unittest.main()

import unittest

from calc import median


class MedianTests(unittest.TestCase):
    def test_odd_number_of_values(self):
        self.assertEqual(median([3, 1, 2]), 2)

    def test_even_number_of_values(self):
        self.assertEqual(median([4, 1, 3, 2]), 2.5)

    def test_single_number(self):
        self.assertEqual(median([7]), 7)

    def test_empty_list_raises_value_error(self):
        with self.assertRaises(ValueError) as error:
            median([])
        self.assertEqual(str(error.exception), "numbers cannot be empty")


if __name__ == '__main__':
    unittest.main()

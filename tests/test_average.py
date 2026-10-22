import unittest

from calc import average


class AverageTests(unittest.TestCase):
    def test_mean_of_four_numbers(self):
        self.assertEqual(average([1, 2, 3, 4]), 2.5)

    def test_single_number(self):
        self.assertEqual(average([10]), 10)

    def test_rounds_to_two_decimal_places(self):
        self.assertEqual(average([1, 2, 2]), 1.67)

    def test_empty_list_raises_value_error(self):
        with self.assertRaises(ValueError) as error:
            average([])
        self.assertEqual(str(error.exception), "numbers cannot be empty")


if __name__ == '__main__':
    unittest.main()

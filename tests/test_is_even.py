import unittest

from calc import is_even


class IsEvenTests(unittest.TestCase):
    def test_four_is_even(self):
        self.assertIs(is_even(4), True)

    def test_seven_is_not_even(self):
        self.assertIs(is_even(7), False)

    def test_zero_is_even(self):
        self.assertIs(is_even(0), True)

    def test_negative_two_is_even(self):
        self.assertIs(is_even(-2), True)

    def test_non_integer_raises_type_error(self):
        with self.assertRaises(TypeError) as error:
            is_even(2.5)
        self.assertEqual(str(error.exception), "n must be an integer")


if __name__ == '__main__':
    unittest.main()

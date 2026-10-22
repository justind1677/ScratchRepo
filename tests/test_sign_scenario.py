import unittest
from calc import sign

class SignScenarioTests(unittest.TestCase):
    def test_negative_numbers(self):
        for value in (-12, -0.5):
            with self.subTest(value=value):
                self.assertEqual(sign(value), -1)
                self.assertIs(type(sign(value)), int)

    def test_zero_including_negative_float_zero(self):
        for value in (0, 0.0, -0.0):
            with self.subTest(value=value):
                self.assertEqual(sign(value), 0)
                self.assertIs(type(sign(value)), int)

    def test_positive_numbers(self):
        for value in (12, 0.5, 1e-300):
            with self.subTest(value=value):
                self.assertEqual(sign(value), 1)
                self.assertIs(type(sign(value)), int)

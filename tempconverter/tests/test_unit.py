import unittest

def celsius_to_fahrenheit(c):
    return round((c * 1.8) + 32, 2)

class TestTempConversion(unittest.TestCase):

    def test_freezing(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_boiling(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)

    def test_body_temp(self):
        self.assertEqual(celsius_to_fahrenheit(37), 98.6)

    def test_negative(self):
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)

    def test_float_input(self):
        self.assertEqual(celsius_to_fahrenheit(20.5), 68.9)

if __name__ == "__main__":
    unittest.main()

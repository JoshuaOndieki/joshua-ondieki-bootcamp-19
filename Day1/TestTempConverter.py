import unittest
from temp_converter import degrees_converter

class TempConverterTest(unittest.TestCase):
    def test_celsius_is_converted_to_farenheit(self):
        """
            F = C * 9/5 + 32
        """
        actual = degrees_converter(10)
        expected = 50
        self.assertEqual(actual,expected,msg = " 10 degrees celsius should be 50 farenheit!")

if __name__ == "__main__":
    unittest.main()

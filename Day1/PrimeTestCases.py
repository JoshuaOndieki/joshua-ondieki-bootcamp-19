#prime numbers function test cases
import unittest
from prime import prime_numbers

class PrimeTest(unittest.TestCase):
    def test_returns_prime_numbers(self):
        self.assertListEqual(prime_numbers(6), [2,3,5], msg="Range of 0-6 should return [2,3,5] as the prime numbers")

    def test_input_is_a_number(self):
        with self.assertRaises(TypeError, msg="Should raise type error if a string is passed as argument"):
            prime_numbers("String")

    def test_return_value_is_list(self):
        self.assertTrue(isinstance(prime_numbers(10), list), msg="The function should return a list")

    def test_returns_None_for_negative_input(self):
        self.assertEqual(prime_numbers(-30),"No prime numbers within that range! All prime numbers are positive",msg="There are no negative primes")

    def test_does_not_return_negative_primes(self):
        self.assertGreater(min(prime_numbers(50)),0)

    def test_does_not_include_non_primes(self):
        self.assertNotIn([0,1,4,6],prime_numbers(6))

if __name__=='__main__':
    unittest.main()

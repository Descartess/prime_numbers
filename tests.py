""" Tests the prime_numbers function"""
import unittest
from primenumber import primenumber, checktype

class PrimeNumberTest(unittest.TestCase):
    """ tests the prime number functions """
    def testdatatype(self):
        """checks that appropriate data type is supplied"""
        args = ["", " ", -1, -1000, "food"]
        with self.assertRaises(TypeError):
            for datatype in args:
                checktype(datatype)
    def testprimenumbers(self):
        """ checks prime numbers under 10"""
        prime_number_list = primenumber(10)
        self.assertEqual(prime_number_list, [2, 3, 5, 7])

unittest.main()

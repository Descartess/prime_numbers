""" Tests the prime_numbers function"""
import unittest
from primenumber import primenumber, checktype

class PrimeNumberTest(unittest.TestCase):
    """ tests the prime number functions """
    def testdatatype(self):
        """checks that appropriate data type is supplied"""
        args = ["", " ", -1, -1000,"food"]
        self.assertRaises(TypeError, checktype, *args)


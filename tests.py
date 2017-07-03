""" Tests the prime_numbers function"""
import unittest
from primenumber import primenumber, checktype

class PrimeNumberTest(unittest.TestCase):
    """ tests the prime number functions """
    def testdatatype(self):
        """checks that appropriate data type is supplied"""
        args = ["", " ", -1, -1000, "food", 16.01, 5.2, -5.5]
        with self.assertRaises(TypeError):
            for datatype in args:
                checktype(datatype)
    def testprimenumbers(self):
        """ checks prime numbers under 10"""
        prime_number_list = primenumber(10)
        self.assertEqual(prime_number_list, [2, 3, 5, 7])
    def testprimenumbersdatatype(self):
        """ test to make sure checktype() is called in primenumber"""
        args = ["", " ", -1, -1000, "food"]
        with self.assertRaises(TypeError):
            for datatype in args:
                primenumber(datatype)
    def testprimenumber_30(self):
        """ test to get prime numbers up 30"""
        prime_number_list = primenumber(30)
        self.assertEqual(prime_number_list, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    def testprimenumber_2(self):
        """ test to get prime numbers up 2"""
        prime_number_list = primenumber(2)
        self.assertEqual(prime_number_list, [])
    def testprimenumber_40(self):
        """ test to get prime numbers up 40"""
        prime_number_list = primenumber(40)
        self.assertEqual(prime_number_list, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])

unittest.main()

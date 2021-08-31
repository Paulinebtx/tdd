import unittest
from main import leapYear

class test_leapYear(unittest.TestCase):
    def test_leap(self):
        self.assertEqual(leapYear(1988), i," is a leap year")
        self.assertEqual(leapYear(1992), i," is a leap year")
        self.assertEqual(leapYear(1996), i," is a leap year")
        self.assertEqual(leapYear(2016), i," is a leap year")
        self.assertEqual(leapYear(2000), i," is a leap year")

    def test_notLeap(self):
        self.assertEqual(leapYear(2015), i," is not a leap year")
        self.assertEqual(leapYear(1800), i," is not a leap year")
        self.assertEqual(leapYear(1700), i," is not a leap year")
        self.assertEqual(leapYear(2100), i," is not a leap year")
        self.assertEqual(leapYear(2200), i," is not a leap year")

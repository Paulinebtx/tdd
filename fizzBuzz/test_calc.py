import unittest
from main import FizzBuzz


class TestFizzBuzz(unittest.TestCase):

    def test_output(self):
        self.assertEqual(FizzBuzz(1), 1)
        self.assertEqual(FizzBuzz(2), 2)
        self.assertEqual(FizzBuzz(4), 4)
        self.assertEqual(FizzBuzz(7), 7)
        self.assertEqual(FizzBuzz(8), 8)

    def test_Fizz(self):
        self.assertEqual(FizzBuzz(3), "Fizz")
        self.assertEqual(FizzBuzz(6), "Fizz")
        self.assertEqual(FizzBuzz(9), "Fizz")
        self.assertEqual(FizzBuzz(12), "Fizz")
        self.assertEqual(FizzBuzz(18), "Fizz")

    def test_Buzz(self):
        self.assertEqual(FizzBuzz(5), "Buzz")
        self.assertEqual(FizzBuzz(10), "Buzz")
        self.assertEqual(FizzBuzz(20), "Buzz")
        self.assertEqual(FizzBuzz(25), "Buzz")
        self.assertEqual(FizzBuzz(35), "Buzz")

    def test_FizzBuzz(self):
        self.assertEqual(FizzBuzz(15), "FizzBuzz")
        self.assertEqual(FizzBuzz(30), "FizzBuzz")
        self.assertEqual(FizzBuzz(45), "FizzBuzz")
        self.assertEqual(FizzBuzz(60), "FizzBuzz")
        self.assertEqual(FizzBuzz(75), "FizzBuzz")



if __name__ == '__main__':
    unittest.main()
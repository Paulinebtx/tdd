import unittest
from main import conv_intRom

class TestConv(unittest.TestCase):

    def test_roman(self):
        self.assertEqual(conv_intRom(1), "I")
        self.assertEqual(conv_intRom(19),"XIX")
        self.assertEqual(conv_intRom(334), "CCCXXXIV")
        self.assertEqual(conv_intRom(14),"XIV")
        self.assertEqual(conv_intRom(7), "VII")

if __name__ == '__main__':
    unittest.main()
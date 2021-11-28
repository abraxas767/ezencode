import unittest
import sys
sys.path.insert(0, "../module/encodings/")
sys.path.insert(0, "../module/encodings/huffman/")
from huffman_encoding import HuffmanEncoding
sys.path.insert(0, "../module/encodings/morse/")
from morse_encoding import MorseEncoding

class UnitTest(unittest.TestCase):
    
    def test_huffman_encoding(self):
        h = HuffmanEncoding()
        test_string0 = 'This is the implementation of the huffman encoding'
        test_string1 = 'BMW'
        test_string2 = '...........'

        res = h.encode(test_string0)
        self.assertEqual(test_string0, h.decode(res))
        res = h.encode(test_string1)
        self.assertEqual(test_string1, h.decode(res))
        res = h.encode(test_string2)
        self.assertEqual(test_string2, h.decode(res))

    def test_morse_encoding(self):
        h = MorseEncoding()
        test_string0 = 'This is the implementation of the morse encoding'
        test_string1 = 'BMW'
        test_string2 = '   '

        res = h.encode(test_string0)
        self.assertEqual(test_string0.upper(), h.decode(res).upper())
        res = h.encode(test_string1)
        self.assertEqual(test_string1.upper(), h.decode(res).upper())
        res = h.encode(test_string2)
        self.assertEqual(test_string2.upper(), h.decode(res).upper())

    def test_empty_huffman_input(self):
        h = HuffmanEncoding()
        s = ''
        self.assertRaises(ValueError, h.encode, s)

    def test_empty_morse_input(self):
        h = MorseEncoding()
        s = ''
        self.assertRaises(ValueError, h.encode, s)

    def test_invalid_morse_input(self):
        h = MorseEncoding()
        s = '#.-$/()'
        self.assertRaises(ValueError, h.encode, s)


if __name__ == "__main__":
    unittest.main()


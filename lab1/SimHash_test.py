import unittest
import SimHash

class TestSimHashMethods(unittest.TestCase):

    def test_calculate_simhash(self):
        text = 'fakultet elektrotehnike i racunarstva'
        expected_simhash = 'f27c6b49c8fcec47ebeef2de783eaf57'
        self.assertEqual(SimHash.calculate_simhash(text), expected_simhash)

    def test_hex_str_to_bin_str(self):
        test_cases = [
            ('ABC', '101010111100'),
            ('000', '000000000000'),
            ('003', '000000000011'),
            ('100', '000100000000'),
            ('F', '1111'),
            ('FFF', '111111111111'),
            ('AB', '10101011')
        ]
        for(hex_str, expected_bin_str) in test_cases:
            self.assertEqual(SimHash._hex_str_to_bin_str(hex_str), expected_bin_str)

    def test_hamming_distance(self):
        test_cases = [
            ('abc', 'abc', 0),
            ('000', '003', 2),
            ('100', '111', 2),
            ('F', 'E', 1),
            ('FFF', 'EEE', 3)
        ]
        for (hex_str1, hex_str2, expected) in test_cases:
            self.assertEqual(SimHash._hamming_distance(hex_str1, hex_str2), expected)

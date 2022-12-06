import unittest
from unittest import TestCase
from src.business.caesar_cipher import CaesarCipher


class TestCeasarCipher(TestCase):
    def setUp(self) -> None:
        self.test_target = CaesarCipher()

    def test_rank1(self):
        natural_rank = 0
        shift = 3
        self.assertEqual(3, self.test_target.calculate_rank(natural_rank, shift))

    def test_rank2(self):
        natural_rank = 1
        shift = 3
        self.assertEqual(4, self.test_target.calculate_rank(natural_rank, shift))

    def test_rank2(self):
        natural_rank = 2
        shift = 5
        self.assertEqual(7, self.test_target.calculate_rank(natural_rank, shift))

    def test_rank3(self):
        natural_rank = 25
        shift = 3
        self.assertEqual(3, self.test_target.calculate_rank(natural_rank, shift))

    def test_rank4(self):
        natural_rank = 23
        shift = 2
        self.assertEqual(0, self.test_target.calculate_rank(natural_rank, shift))

    def test_rank5(self):
        natural_rank = 20
        shift = -4
        self.assertEqual(16, self.test_target.calculate_rank(natural_rank, shift))

    def test_rank6(self):
        natural_rank = 5
        shift = -2
        self.assertEqual(3, self.test_target.calculate_rank(natural_rank, shift))

    def test_rank7(self):
        natural_rank = 1
        shift = -3
        self.assertEqual(23, self.test_target.calculate_rank(natural_rank, shift))

    def test_ceasar_cipher_encode(self):
        message = "CAT"
        shift = 3
        self.assertEqual("FDW", self.test_target.ceasar_cipher(message, shift))

    def test_ceasar_cipher_decode(self):
        message = "FDW"
        shift = -3
        self.assertEqual("CAT", self.test_target.ceasar_cipher(message, shift))

    def test_ceasar_cipher_case_insensitive(self):
        message = "Cat"
        shift = 3
        self.assertEqual("FDW", self.test_target.ceasar_cipher(message, shift))

    def test_sentence(self):
        message = "the fat cat"
        shift = 3
        self.assertEqual("WKH IDW FDW",self.test_target.ceasar_cipher(message,shift))


if __name__ == '__main__':
    unittest.main()

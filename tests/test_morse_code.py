import unittest
from unittest import TestCase
from src.business.morse_code import MorseCode


class TestMorseCode(TestCase):
    def setUp(self) -> None:
        self.test_target = MorseCode()

    def test_morse_code(self):
        morse_message = '-.. . -.-. --- -.. . / -- --- .-. ... .'
        self.assertEqual("DECODE MORSE", self.test_target.message_decode(morse_message))


    def test_encode(self):
        alphabet_message = 'D E C O D E / M O R S E'
        self.assertEqual("-...-.-.----.../-----.-.....",self.test_target.message_encode(alphabet_message))

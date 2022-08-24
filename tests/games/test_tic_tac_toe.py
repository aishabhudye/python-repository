import unittest
from unittest import TestCase

from src.games.tic_tac_toe import TicTacToe


class MyTestCase(TestCase):
    def setUp(self) -> None:
        self.test_target = TicTacToe()

    def test_reverse(self):
        self.test_target.generate()


if __name__ == '__main__':
    unittest.main()
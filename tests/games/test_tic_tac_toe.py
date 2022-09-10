import unittest
from unittest import TestCase

from src.games.tic_tac_toe import TicTacToe


class GamesTestCase(TestCase):
    def setUp(self) -> None:
        self.test_target = TicTacToe()

    def test_all_locations_are_not_populated_scenario_1(self):
        noughts_crosses_array = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.assertFalse(self.test_target.board_is_full(noughts_crosses_array), "Scenario 1")

    def test_all_locations_are_not_populated_scenario_2(self):
        noughts_crosses_array = [" ", " ", " ", " ", " ", " ", " ", " ", "X"]
        self.assertFalse(self.test_target.board_is_full(noughts_crosses_array), "Scenario 2")

    def test_all_locations_are_not_populated_scenario_3(self):
        """ There is an O instead of a zero at the second location"""
        noughts_crosses_array = ["X", "O", "X", "0", "X", "0", "X", "0", "X"]
        self.assertFalse(self.test_target.board_is_full(noughts_crosses_array), "Scenario 3")

    def test_all_locations_are_populated_scenario_4(self):
        noughts_crosses_array = ["X", "0", "X", "0", "X", "0", "X", "0", "X"]
        self.assertTrue(self.test_target.board_is_full(noughts_crosses_array), "Scenario 4")


if __name__ == '__main__':
    unittest.main()

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

    def test_verify_input_scenario1(self):
        self.assertEqual((0, 'X'), self.test_target.verify_input("0:X"), "verify_input_scenario1: +ve")

    def test_verify_input_scenario2(self):
        self.assertEqual((8, '0'), self.test_target.verify_input("8:0"), "verify_input_scenario2: +ve")

    def test_verify_input_scenario3(self):
        self.assertEqual((-1, '!'), self.test_target.verify_input("9:X"), "verify_input_scenario3: -ve")

    def test_verify_input_scenario4(self):
        self.assertEqual((-1, '!'), self.test_target.verify_input("8:Y"), "verify_input_scenario4: -ve")

    def test_verify_input_scenario5(self):
        self.assertEqual((-1, '!'), self.test_target.verify_input("9:Z"), "verify_input_scenario5: -ve")


if __name__ == '__main__':
    unittest.main()

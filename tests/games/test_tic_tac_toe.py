import unittest
from unittest import TestCase

from src.games.tic_tac_toe import validate_input, someone_has_won, board_is_full


class GamesTestCase(TestCase):

    def test_all_locations_are_not_populated_scenario_1(self):
        noughts_crosses_array = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.assertFalse(board_is_full(noughts_crosses_array), "Scenario 1")

    def test_all_locations_are_not_populated_scenario_2(self):
        noughts_crosses_array = [" ", " ", " ", " ", " ", " ", " ", " ", "X"]
        self.assertFalse(board_is_full(noughts_crosses_array), "Scenario 2")

    def test_all_locations_are_not_populated_scenario_3(self):
        """ There is an O instead of a zero at the second location"""
        noughts_crosses_array = ["X", "O", "X", "0", "X", "0", "X", "0", "X"]
        self.assertFalse(board_is_full(noughts_crosses_array), "Scenario 3")

    def test_all_locations_are_populated_scenario_4(self):
        noughts_crosses_array = ["X", "0", "X", "0", "X", "0", "X", "0", "X"]
        self.assertTrue(board_is_full(noughts_crosses_array), "Scenario 4")

    def test_verify_input_scenario1(self):
        self.assertEqual((0, 'X'), validate_input("0:X"), "verify_input_scenario1: +ve")

    def test_verify_input_scenario2(self):
        self.assertEqual((8, '0'), validate_input("8:0"), "verify_input_scenario2: +ve")

    def test_verify_input_scenario3(self):
        self.assertEqual((-1, '!'), validate_input("9:X"), "verify_input_scenario3: -ve")

    def test_verify_input_scenario4(self):
        self.assertEqual((-1, '!'), validate_input("8:Y"), "verify_input_scenario4: -ve")

    def test_verify_input_scenario5(self):
        self.assertEqual((-1, '!'), validate_input("9:Z"), "verify_input_scenario5: -ve")

    def test_nought_has_won_scenario1(self):
        noughts_crosses_array = ["0", "0", "0", " ", " ", " ", " ", " ", " "]
        self.assertTrue(someone_has_won(noughts_crosses_array))

    def test_nought_has_won_scenario2(self):
        noughts_crosses_array = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
        self.assertTrue(someone_has_won(noughts_crosses_array))

    def test_nought_has_won_scenario3(self):
        noughts_crosses_array = ["", "", "", "0", "0", "0", " ", " ", " "]
        self.assertTrue(someone_has_won(noughts_crosses_array))

    def test_nought_has_won_scenario4(self):
        noughts_crosses_array = ["", "", "", "X", "X", "X", " ", " ", " "]
        self.assertTrue(someone_has_won(noughts_crosses_array))

    def test_nought_has_won_scenario5(self):
        noughts_crosses_array = ["", "", "", "", "", "", "0", "0", "0"]
        self.assertTrue(someone_has_won(noughts_crosses_array))

    def test_nought_has_won_scenario6(self):
        noughts_crosses_array = ["", "", "", "", "", "", "X", "X", "X"]
        self.assertTrue(someone_has_won(noughts_crosses_array))

    def test_nought_has_won_scenario7(self):
        noughts_crosses_array = ["0", "", "", "0", "", "", "0", "", ""]
        self.assertTrue(someone_has_won(noughts_crosses_array))

    def test_nought_has_won_scenario8(self):
        noughts_crosses_array = ["X", "", "", "X", "", "", "X", "", ""]
        self.assertTrue(someone_has_won(noughts_crosses_array))

    def test_nought_has_won_scenario9(self):
        noughts_crosses_array = ["", "0", "", "", "0", "", "", "0", ""]
        self.assertTrue(someone_has_won(noughts_crosses_array))

    def test_nought_has_won_scenario10(self):
        noughts_crosses_array = ["", "X", "", "", "X", "", "", "X", ""]
        self.assertTrue(someone_has_won(noughts_crosses_array))

    def test_nought_has_won_scenario11(self):
        noughts_crosses_array = ["", "", "0", "", "", "0", "", "", "0"]
        self.assertTrue(someone_has_won(noughts_crosses_array))

    def test_nought_has_won_scenario12(self):
        noughts_crosses_array = ["", "", "X", "", "", "X", "", "", "X"]
        self.assertTrue(someone_has_won(noughts_crosses_array))

    def test_nought_has_won_scenario13(self):
        noughts_crosses_array = ["0", "", "", "", "0", "", "", "", "0"]
        self.assertTrue(someone_has_won(noughts_crosses_array))

    def test_nought_has_won_scenario14(self):
        noughts_crosses_array = ["X", "", "", "", "X", "", "", "", "X"]
        self.assertTrue(someone_has_won(noughts_crosses_array))

    def test_nought_has_won_scenario15(self):
        noughts_crosses_array = ["", "", "0", "", "0", "", "0", "", ""]
        self.assertTrue(someone_has_won(noughts_crosses_array))

    def test_nought_has_won_scenario16(self):
        noughts_crosses_array = ["", "", "X", "", "X", "", "X", "", ""]
        self.assertTrue(someone_has_won(noughts_crosses_array))

    def test_bug_scenario_X_X_0_wins(self):
        noughts_crosses_array = ["X", "X", "0", "", "", "", "", "", ""]
        self.assertFalse(someone_has_won(noughts_crosses_array))


if __name__ == '__main__':
    unittest.main()

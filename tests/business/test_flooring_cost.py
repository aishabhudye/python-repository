from unittest import TestCase

from src.business.flooring_cost import FlooringCost


class TestFlooringCost(TestCase):

    def setUp(self) -> None:
        self.test_target = FlooringCost()
    """
    Positive test case: Max Length of room = 3.0m, Width of room = 4.0m. Therefore cost will be £120.00
    """
    def test_scenario_1(self):
        self.assertEqual(120.00, self.test_target.calculate_cost(3.0, 4.0))

    """
    Negative test case: Max Length of room = 0m, Width of room = 5.0m. Therefore cost will be £0.00
    """
    def test_scenario_2(self):
        self.assertEqual(0.00, self.test_target.calculate_cost(0.0, 5.0))

    """
    Test case: Max Length of room = 5m, Width of room = 3.0m. Therefore cost will be £150.00
    """
    def test_scenario_3(self):
        self.assertEqual(150.00, self.test_target.calculate_cost(5.0, 3.0))

    """
    Test case: Max Length of room = 5m, Width of room = 4.0m. Therefore cost will be £200.00
    """
    def test_scenario_4(self):
        self.assertEqual(200.00, self.test_target.calculate_cost(5.0, 4.0))

    """
    Test case: Max Length of room = 3m, Width of room = 2.0m. Therefore cost will be £60.00
    """
    def test_scenario_5(self):
        self.assertEqual(60.00, self.test_target.calculate_cost(3.0, 2.0))

    """
    Test case: Max Length of room = 3.9m, Width of room = 2.0m. Therefore cost will be £78.00
    """
    def test_scenario_6(self):
        self.assertEqual(78.00, self.test_target.calculate_cost(3.9, 2.0))

    """
    Test case: Max Length of room = 6.0m, Width of room = 5.0m. Therefore cost will be £300.00
    """
    def test_scenario_7(self):
        self.assertEqual(0.00, self.test_target.calculate_cost(6.0, 5.0))





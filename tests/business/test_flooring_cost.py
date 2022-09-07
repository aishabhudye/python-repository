from unittest import TestCase

from src.business.flooring_cost import FlooringCost


class TestFlooringCost(TestCase):

    def setUp(self) -> None:
        self.test_target = FlooringCost()
    """
    Positive test case: Max Length of room = 3.0m, Width of room = 4.0m. Therefore cost will be £120.00
    """
    def test_positive_scenario_1(self):
        self.assertEqual(120.00, self.test_target.calculate_cost(3.0, 4.0))

    """
    Positive test case: Max Length of room = 3.0m, Width of room = 4.0m. Therefore cost will be £120.00
    """
    def test_positive_scenario_1(self):
        self.assertEqual(120.00, self.test_target.calculate_cost(3.0, 4.0))


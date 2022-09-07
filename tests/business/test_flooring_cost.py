from unittest import TestCase


class TestFlooringCost(TestCase):

    def test_print_total_cost_information(self):
        self.test_target.print_length_and_width_and_total_cost_information()
        pass

    def test_calculate_cost(self):
        self.assertEqual(self.test_target.calculate_total())


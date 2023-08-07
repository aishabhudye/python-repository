import unittest

from src.maths.quadratic import determine_roots


class MathsProcessorTestCase(unittest.TestCase):

    def test_2_distinct_real_roots(self):
        """
        x*x -4*x +3 = 0
        """
        self.assertEqual("2 distinct real roots", determine_roots(1, -4, 3))

    def test_single_real_root(self):
        """
        x*x -2*x +1 = 0
        """
        self.assertEqual("single real root", determine_roots(1, -2, 1))

    def test_no_real_root(self):
        """
        x*x +1 = 0
        """
        self.assertEqual("no real roots", determine_roots(1, 0, 1))


if __name__ == '__main__':
    unittest.main()

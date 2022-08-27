import unittest

from src.maths.quadratic import MathsProcessor


class MathsProcessorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.test_target = MathsProcessor()

    def test_2_distinct_real_roots(self):
        """
        x*x -4*x +3 = 0
        """
        self.assertEqual("2 distinct real roots", self.test_target.determine_roots(1, -4, 3))

    def test_single_real_root(self):
        """
        x*x -2*x +1 = 0
        """
        self.assertEqual("single real root", self.test_target.determine_roots(1, -2, 1))

    def test_no_real_root(self):
        """
        x*x +1 = 0
        """
        self.assertEqual("no real roots", self.test_target.determine_roots(1, 0, 1))


if __name__ == '__main__':
    unittest.main()

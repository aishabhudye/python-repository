import unittest

from src.strings.string_processing import StringProcessor


class StringProcessingTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.test_target = StringProcessor()

    def test_reverse(self):
        sibling_array = ["Aisha", "Hafsa", "Talha"]
        sibling_array_in_reverse = ["Talha", "Hafsa", "Aisha"]
        self.assertEqual(sibling_array_in_reverse, self.test_target.reverse_array(sibling_array))


if __name__ == '__main__':
    unittest.main()

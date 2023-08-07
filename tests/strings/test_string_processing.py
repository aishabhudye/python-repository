import unittest

from src.strings.string_processing import reverse_array


class StringProcessingTestCase(unittest.TestCase):

    def test_reverse(self):
        sibling_array = ["Aisha", "Hafsa", "Talha"]
        sibling_array_in_reverse = ["Talha", "Hafsa", "Aisha"]
        self.assertEqual(sibling_array_in_reverse, reverse_array(sibling_array))


if __name__ == '__main__':
    unittest.main()

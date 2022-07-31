import unittest

from string_processing import StringProcessor


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.test_targettarget = StringProcessor()

    def test_reverse(self):
        sibling_array = ["Aisha", "Hafsa", "Talha"]
        sibling_array_in_reverse = ["Talha", "Hafsa", "Aisha"]
        self.assertEqual(self.test_targettarget.reverse_array(sibling_array), sibling_array_in_reverse)


if __name__ == '__main__':
    unittest.main()

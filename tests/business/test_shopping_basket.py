import unittest
from unittest import TestCase

from src.business.shopping_basket import calculate_total

'''
The products dictionary / hash table / hash map holds a value (product price) mapped against a key (product identifer)
e.g. The key 'Lemon' maps to the value of £0.50 => Each lemon costs £0.50
'''
products = {'Lemon': 0.50, 'Apple': 0.75, 'Orange': 0.65, 'Melon': 1.00, 'Pineapple': 1.50, 'Mango': 1.25}

'''
The basket dictionary / hash table / hash map holds a value (the number of a particular product) mapped against a key (product identifer)
e.g. The key 'Lemon' maps to the value of 4 => There are 4 individual lemons in the shopping basket
'''
basket = {'Lemon': 4, 'Apple': 4, 'Orange': 3, 'Melon': 1, 'Pineapple': 1, 'Mango': 2}


class GamesTestCase(TestCase):

    def test_basket_total(self):
        self.assertEqual(11.95, calculate_total(products, basket))


if __name__ == '__main__':
    unittest.main()


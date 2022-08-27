class ShoppingBasket:

    def calculate_total(self, products, basket):
        print('We are the {} who say "{}!"'.format('knights', 'Ni'))

    def print_product_and_basket_information(self, products, basket):

        """Iterate over both keys and values"""
        print("About to print products information by iterating over dictionary keys and values")
        for key, value in products.items():
            print('The price of {} is {}'.format(key, value))

        """Iterate over key and then retrieve value based on key"""
        print()
        print("About to print products information by iterating over dictionary keys and then retrieving value based on key")
        for key in products.keys():
            print('The price of {} is {}'.format(key, products[key]))

        """Iterate over both keys and values"""
        print()
        print()
        print("About to print basket information by iterating over dictionary keys and values")
        for key, value in basket.items():
            print('The price of {} is {}'.format(key, value))

        """Iterate over key and then retrieve value based on key"""
        print()
        print("About to print basket information by iterating over dictionary keys and then retrieving value based on key")
        for key in basket.keys():
            print('The price of {} is {}'.format(key, basket[key]))


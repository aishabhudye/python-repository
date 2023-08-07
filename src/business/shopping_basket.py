def calculate_total(products, basket):
    grand_total = 0.0
    for key, value in basket.items():
        print('The price of {} is {}'.format(key, products[key]))
        print('The number of {} in my basket is {}'.format(key, basket[key]))
        total = products[key] * basket[key]
        grand_total = grand_total + total

    return grand_total


def print_product_and_basket_information(products, basket):

    """Iterate over both keys and values"""
    print("About to print products information by iterating over dictionary keys and values")
    for key, value in products.items():
        print('The price of {} is {}'.format(key, value))

    """Iterate over key and then retrieve value based on key"""
    print()
    print(
        "About to print products information by iterating over dictionary keys and then retrieving value based on key")
    for key in products.keys():
        print('The price of {} is £{}'.format(key, products[key]))

    """Iterate over both keys and values"""
    print()
    print()
    print("About to print basket information by iterating over dictionary keys and values")
    for key, value in basket.items():
        print('The number of {} in my basket is {}'.format(key, value))

    """Iterate over key and then retrieve value based on key"""
    print()
    print(
        "About to print basket information by iterating over dictionary keys and then retrieving value based on key")
    for key in basket.keys():
        print('The price of {} is {}'.format(key, basket[key]))







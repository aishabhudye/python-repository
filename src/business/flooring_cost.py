class FlooringCost:

    def calculate_cost(self):
        total_cost = 0.0
        length = input("Enter the length of your floor.")
        width = input("Enter the width of your floor")
        if length <= 0:
            print("ERROR")
        elif width > 4:
            print("ERROR")
        else:
            total_cost = length * width * 10
            print('The total cost of installing carpet in a room of length {} and width {} is {}'.format(total_cost))
        return total_cost



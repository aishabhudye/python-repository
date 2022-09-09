class FlooringCost:

    def calculate_cost_given_inputs(self):
        length = input("Enter the length of your floor.")
        width = input("Enter the width of your floor")
        return self.calculate_cost(length, width)

    def calculate_cost(self, length, width):
        if length <= 0:
            print("ERROR")
            total_cost = 0.0
        elif width > 4:
            print("ERROR")
            total_cost = 0.0
        else:
            total_cost = length * width * 10
            print('The total cost of installing carpet in a room of length {} and width {} is {}'.format(length, width, total_cost))
        return total_cost



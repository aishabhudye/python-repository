class TicTacToe:

    def display_instructions_with_board(self):
        print('Please specify which position/location you want your item to be as follows (0:X or 8:O)')
        print('The positions themselves are as follows')
        tic_tac_toe_locations = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        self.print_noughts_crosses_on_board(tic_tac_toe_locations)
        noughts_crosses_array = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        while self.board_is_not_full(noughts_crosses_array):
            location_value = input(
                'Please specify which position/location you want your item to be as follows (0:X or 8:O) -> ')
            input_array = location_value.split(":")
            location = int(input_array[0])
            value_at_location = input_array[1]
            noughts_crosses_array[location] = value_at_location
            self.print_noughts_crosses_on_board(noughts_crosses_array)

    @staticmethod
    def print_noughts_crosses_on_board(array_parameter):
        print('|{}|{}|{}|'.format(array_parameter[0], array_parameter[1], array_parameter[2]))
        print('|{}|{}|{}|'.format(array_parameter[3], array_parameter[4], array_parameter[5]))
        print('|{}|{}|{}|'.format(array_parameter[6], array_parameter[7], array_parameter[8]))

    @staticmethod
    def board_is_full(array_parameter):
        populated_location_count = 0
        empty_location_count = 0
        for item in array_parameter:
            if item == "X" or item == "0":
                populated_location_count += 1
            else:
                empty_location_count += 1
        if populated_location_count == 9:
            return True
        else:
            return False

    def board_is_not_full(self, array_parameter):
        return not self.board_is_full(array_parameter)

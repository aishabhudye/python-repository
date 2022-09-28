class TicTacToe:

    def display_instructions_with_board(self):
        print('Please specify which position/location you want your item to be as follows (0:X or 8:O)')
        print('The positions themselves are as follows')
        tic_tac_toe_locations = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        self.print_board(tic_tac_toe_locations)
        noughts_crosses_array = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        previous_location = -1
        previous_value = ''
        while self.board_is_not_full(noughts_crosses_array):
            user_input = input(
                'Please specify which position/location you want your item to be as follows (0:X or 8:O) -> ')
            current_location, current_value = self.validate_input(user_input)
            '''If the user input is correct, carry on, else prompt for input'''
            user_input_is_invalid = current_location == -1 and current_value == '!'
            duplicate_attempt = False
            # print('CURRENT:{}->{} ; PREVIOUS:{}->{}'.format(current_location, current_value, previous_location,
            #                                                 previous_value))
            if previous_value == current_value or previous_location == current_location:
                duplicate_attempt = True
            while user_input_is_invalid or duplicate_attempt:
                user_input = input(
                    'Please specify which position/location you want your item to be as follows (0:X or 8:O) -> ')
                current_location, current_value = self.validate_input(user_input)
                duplicate_attempt = False

            '''Store current value in previous value for comparison in the next iteration'''
            previous_location = current_location
            previous_value = current_value
            noughts_crosses_array[current_location] = current_value
            self.print_board(noughts_crosses_array)

            '''We need to check whether X or 0 has won at this point'''
            if self.someone_has_won(noughts_crosses_array):
                print('{} has won'.format(current_value))
                break

    '''
    This returns a boolean flag either True or False
    '''
    def someone_has_won(self, noughts_crosses_array):
        win_in_a_row = self.someone_has_won_in_a_row(noughts_crosses_array)
        win_in_a_column = self.someone_has_won_in_a_column(noughts_crosses_array)
        win_in_diagonal = self.someone_has_won_in_diagonal(noughts_crosses_array)
        if win_in_a_row or win_in_a_column or win_in_diagonal:
            return True
        else:
            return False

    def someone_has_won_in_diagonal(self, noughts_crosses_array):
        win = False
        if noughts_crosses_array[0] == '0' and noughts_crosses_array[4] == '0' and noughts_crosses_array[8] == '0':
            win = True
        if noughts_crosses_array[0] == 'X' and noughts_crosses_array[4] == 'X' and noughts_crosses_array[8] == 'X':
            win = True
        if noughts_crosses_array[2] == '0' and noughts_crosses_array[4] == '0' and noughts_crosses_array[6] == '0':
            win = True
        if noughts_crosses_array[2] == 'X' and noughts_crosses_array[4] == 'X' and noughts_crosses_array[6] == 'X':
            win = True
        return win

    def someone_has_won_in_a_column(self, noughts_crosses_array):
        win = False
        if noughts_crosses_array[0] == '0' and noughts_crosses_array[3] == '0' and noughts_crosses_array[6] == '0':
            win = True
        if noughts_crosses_array[0] == 'X' and noughts_crosses_array[3] == 'X' and noughts_crosses_array[6] == 'X':
            win = True
        if noughts_crosses_array[1] == '0' and noughts_crosses_array[4] == '0' and noughts_crosses_array[7] == '0':
            win = True
        if noughts_crosses_array[1] == 'X' and noughts_crosses_array[4] == 'X' and noughts_crosses_array[7] == 'X':
            win = True
        if noughts_crosses_array[2] == '0' and noughts_crosses_array[5] == '0' and noughts_crosses_array[8] == '0':
            win = True
        if noughts_crosses_array[2] == 'X' and noughts_crosses_array[5] == 'X' and noughts_crosses_array[8] == 'X':
            win = True
        return win

    def someone_has_won_in_a_row(self, noughts_crosses_array):
        win = False
        if noughts_crosses_array[0] == '0' and noughts_crosses_array[1] == '0' and noughts_crosses_array[2] == '0':
            win = True
        if noughts_crosses_array[0] == 'X' and noughts_crosses_array[1] == 'X' and noughts_crosses_array[2] == 'X':
            win = True
        if noughts_crosses_array[3] == '0' and noughts_crosses_array[4] == '0' and noughts_crosses_array[5] == '0':
            win = True
        if noughts_crosses_array[3] == 'X' and noughts_crosses_array[4] == 'X' and noughts_crosses_array[5] == 'X':
            win = True
        if noughts_crosses_array[6] == '0' and noughts_crosses_array[7] == '0' and noughts_crosses_array[8] == '0':
            win = True
        if noughts_crosses_array[6] == 'X' and noughts_crosses_array[7] == 'X' and noughts_crosses_array[8] == 'X':
            win = True
        return win

    """Here we need to validate the location/address from 0 to 8 - the pigeon hole name"""
    """Here we need to validate the value at the location/address from 0 to 8 - the pigeon hole content either 0 or X"""

    def validate_input(self, location_value):
        input_array = location_value.split(":")
        location = int(input_array[0])
        value_at_location = input_array[1]
        X = input_array
        """If the input is invalid in anyway, return a special flag/value"""
        location_is_valid = (0 <= location <= 8)
        value_is_valid = value_at_location == 'X' or value_at_location == "0"
        if location_is_valid and value_is_valid:
            return location, value_at_location
        else:
            """The tuple (1, """
            return -1, '!'

    @staticmethod
    def print_board(array_parameter):
        print('|{}|{}|{}|'.format(array_parameter[0], array_parameter[1], array_parameter[2]))
        print('|{}|{}|{}|'.format(array_parameter[3], array_parameter[4], array_parameter[5]))
        print('|{}|{}|{}|'.format(array_parameter[6], array_parameter[7], array_parameter[8]))

    @staticmethod
    def board_is_full(array_parameter):
        populated_location_count = 0
        empty_location_count = 0
        for item in array_parameter:
            if item == 'X' or item == '0':
                populated_location_count += 1
            else:
                empty_location_count += 1
        if populated_location_count == 9:
            return True
        else:
            return False

    def board_is_not_full(self, array_parameter):
        return not self.board_is_full(array_parameter)

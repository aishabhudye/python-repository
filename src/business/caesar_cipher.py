def calculate_rank(natural_rank, shift):
    cipher_rank = (natural_rank + shift) % 25
    return cipher_rank


class CaesarCipher:
    number_to_letter_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',
                             11: 'L', 12: 'M', 13: 'N', 14: 'O',
                             15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
                             25: 'Z'}
    letter_to_number_dict = {v: k for k, v in number_to_letter_dict.items()}

    def user_input(self):
        user_input = input('Enter your message ')
        shift_user_input = int(input('Enter the shift:+ for right and - for left'))
        self.caesar_cipher(user_input, shift_user_input)

    def caesar_cipher(self, user_input, shift):
        message = user_input
        list_of_letters = []
        for item in message:
            list_of_letters.append(item)
            print(list_of_letters)
        cipher_message = ''
        for letter in list_of_letters:
            if letter == ' ':
                cipher_letter = ' '
            else:
                natural_rank = self.letter_to_number_dict[letter.upper()]
                cipher_rank = calculate_rank(natural_rank, shift)
                cipher_letter = self.number_to_letter_dict[cipher_rank]

            cipher_message = cipher_message + cipher_letter

        return cipher_message

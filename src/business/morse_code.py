class MorseCode:
    morse_code_to_alphabet_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                                   'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                                   'O': '---', 'P': '.--.',
                                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
                                   'X': '-..-',
                                   'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
                                   '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                                   '9': '----.', ' ': ' '}

    def message_decode(self, morse_encoded_message):
        alphabet_to_morse_code = {v: k for k, v in self.morse_code_to_alphabet_dict.items()}

        list_of_morse_characters = morse_encoded_message.split()
        decoded_message = ''
        for morse_character in list_of_morse_characters:
            print(morse_character)
            if morse_character == '/':
                morse_character = ' '
            letter = alphabet_to_morse_code[morse_character]
            decoded_message = decoded_message + letter

        return decoded_message


    def message_encode(self,morse_decoded_message):
        morse_code_to_alphabet_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                                       'G': '--.',
                                       'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
                                       'N': '-.',
                                       'O': '---', 'P': '.--.',
                                       'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
                                       'W': '.--',
                                       'X': '-..-',
                                       'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
                                       '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                                       '8': '---..',
                                       '9': '----.', '/': '/'}
        list_alphabet_characters = morse_decoded_message.split()
        encoded_message = ''
        for alphabet_character in list_alphabet_characters:
            print(alphabet_character)
            if alphabet_character == '/':
                alphabet_character = '/'
            morse = morse_code_to_alphabet_dict[alphabet_character]
            encoded_message = encoded_message + morse

        return encoded_message


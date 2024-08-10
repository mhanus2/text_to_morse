from text_to_morse.constants import MORSE_CODES
from text_to_morse.exceptions import UnknownCharacterError


class TextToMorseConverter:
    def __init__(self):
        self._morse = MORSE_CODES

    def convert_to_morse(self, text: str) -> str:
        """Converts given text to morse code.

        Parameters
        ----------
        text : str
            Text for converting to morse

        Returns
        -------
        str
            Morse code
        """
        result = []
        for char in text:
            try:
                result.append(self._morse[char.upper()])
            except KeyError:
                print(f"You entered unknown character - {char}!")
                raise UnknownCharacterError
        return ' '.join(result)


if __name__ == "__main__":
    text_to_morse_converter = TextToMorseConverter()
    active = True
    while active:
        inputted_text = input("Please enter a text you want to convert: ")

        try:
            morse_code = text_to_morse_converter.convert_to_morse(inputted_text)
        except UnknownCharacterError:
            active = False
        else:
            print(f"Converted morse code:\n {morse_code}")

            another = None
            while another not in ["y", "n"]:
                another = input("Do you want to convert another text? (y/n) ")

                if another == "y":
                    break
                elif another == "n":
                    active = False
                    break
                else:
                    print("Please enter only y or n.")

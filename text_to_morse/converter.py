class TextToMorseConverter:
    @staticmethod
    def convert_to_morse(text: str) -> str:
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
        print(f"Converting {text}")
        return text


if __name__ == "__main__":
    text_to_morse_converter = TextToMorseConverter()
    active = True
    while active:
        inputted_text = input("Please enter a text you want to convert: ")
        morse_code = text_to_morse_converter.convert_to_morse(inputted_text)
        print(f"Converted morsed code: {morse_code}")

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
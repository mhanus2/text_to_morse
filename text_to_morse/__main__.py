from text_to_morse.text_to_morse_converter import TextToMorseConverter


def main():
    text_to_morse_converter = TextToMorseConverter()

    active = True
    while active:
        text = input("Please enter a text you want to convert: ")
        morse_code = text_to_morse_converter.convert_to_morse(text)
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


if __name__ == "__main__":
    main()

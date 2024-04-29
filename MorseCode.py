import argparse

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

parser = argparse.ArgumentParser()
parser.add_argument("input_text", help="The text to be encoded into Morse code or decoded from Morse code")
parser.add_argument("output_file", help="The file to save the result")

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-e", "--encode", action="store_true", help="Encode the text into Morse code")
group.add_argument("-d", "--decode", action="store_true", help="Decode the Morse code")

args = parser.parse_args()


def encode_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append(' ')
    return ' '.join(morse_code)


def decode_from_morse(morse_code):
    inverted_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    decoded_text = []
    for code in morse_code.split(' '):
        if code in inverted_dict:
            decoded_text.append(inverted_dict[code])
        else:
            decoded_text.append(' ')
    return ''.join(decoded_text)


def encode_or_decode(text, output_filename, encode=False, decode=False):
    if encode:
        result = encode_to_morse(text)
    elif decode:
        result = decode_from_morse(text)
    else:
        raise ValueError("Please specify either --encode or --decode option")

    with open(output_filename, 'w') as file:
        file.write(result)
    print(f"Result has been written to {output_filename}")


encode_or_decode(args.input_text, args.output_file, args.encode, args.decode)

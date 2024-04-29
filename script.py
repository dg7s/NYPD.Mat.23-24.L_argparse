import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="The file to be read")
parser.add_argument("result_file", help="The file to save result")
parser.add_argument("-s", "--shift", type=int, default=3,
                    help="The number of places to shift each letter (default: 3).")

args = parser.parse_args()


def encrypt_file(input_filename, output_filename, shift):
    with open(input_filename, 'r', encoding='utf-8') as file:
        original_text = file.read()

    encrypted_text = []
    for char in original_text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text.append(new_char)
        else:
            encrypted_text.append(char)
    encrypted_text = ''.join(encrypted_text)

    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(encrypted_text)
    print(f"Encrypted text has been written to {output_filename}")


encrypt_file(args.input_file, args.output_file, args.shift)

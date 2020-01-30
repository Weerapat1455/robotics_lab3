input = "The sunset sets at twelve o'clock"


def alphabet_position(input):
    alphabet = ""
    input = input.lower()
    for character in input:
        if character != ' ':
            number = ord(character) - 96
            if 0 < number <= 26:
                alphabet += str(number)
                alphabet += ' '
    return alphabet.strip()
alphabet = alphabet_position(input)
print(alphabet)

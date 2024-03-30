import pyperclip
import string


FINISH_TRIGGER = ":wq"


def multiple_lines_input(input_text):
    """
    Takes multiple lines of input from the user and returns them as a list of strings.
    :param input_text: The text to display before taking the input
    :return: A list of strings containing the input
    """
    print(input_text)

    contents = []
    while not (line := input()) == FINISH_TRIGGER:
        contents.append(line + "\n")

    return contents        # Discarding the TRIGGER from the input


def get_first_letter_index(line):
    for i in range(len(line)):
        if (line[i].isalpha()) or (line[i] in string.punctuation):
            return i

    return -1


def add_grave_accents(code):
    modified_code = []

    for line in code:
        line_start = get_first_letter_index(line)

        if line_start == -1:
            modified_code.append("\n")
            continue

        modified_code.append(line[:line_start] + "`" + line.rstrip()[line_start:] + "`\n")

    return modified_code


def main():
    code = multiple_lines_input(f"Enter the code to format (Type {FINISH_TRIGGER} to finish):")
    pyperclip.copy("".join(add_grave_accents(code)))
    print("".join(add_grave_accents(code)))


if __name__ == "__main__":
    main()

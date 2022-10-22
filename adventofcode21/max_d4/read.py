from collections import namedtuple
from curses.ascii import isdigit
from io import TextIOWrapper
import re
from black import is_number_token
import numpy as np

day_4_input = namedtuple("day_4_input", ["random_numbers", "bingo_matrices"])


def get_input() -> day_4_input:
    with open("input", "r") as f:
        random_numbers = get_random_numbers(f)
        bingo_matrices = []
        while True:
            try:
                matrix = get_next_bingo_matrix(f)
                bingo_matrices.append(matrix)
            except EOFError:
                break

    return random_numbers, bingo_matrices


def get_random_numbers(f: TextIOWrapper):
    header = f.readline().strip("\n")
    numbers = [int(number) for number in header.split(",")]
    return numbers


def get_next_bingo_matrix(f, matrix_length=5):
    empty_line = f.readline()
    assert is_empty(empty_line)

    if empty_line == "":  # EOF
        raise EOFError("EOF!")

    bingo_lines = [f.readline() for _ in range(matrix_length)]
    matrix = [
        [int(number) for number in line_to_numbers(line)]
        for line in bingo_lines
    ]
    return np.array(matrix)


def is_empty(line):
    return line == "" or line == "\n"


def line_to_numbers(line: str):
    """
    >>> line = " 1 2, 3   5   100"
    >>> line_to_numbers(line)
    [1, 2, 3, 5, 100]
    """
    numbers = []
    number_start = None

    for i, c in enumerate(line):
        if i == 0:
            if c.isdigit():
                number_start = i
            continue

        if number_start is None:
            if c.isdigit():
                number_start = i
        elif not c.isdigit():
            digits = line[number_start:i]
            numbers.append(int(digits))
            number_start = None

        if i + 1 == len(line):  # last character
            if c.isdigit():
                digits = line[number_start : i + 1]
                numbers.append(int(digits))

    return numbers


if __name__ == "__main__":
    random_numbers, bingo = get_input()
    print(random_numbers)
    print(bingo[0])

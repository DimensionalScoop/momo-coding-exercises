from collections import namedtuple
from numpy.typing import NDArray
import numpy as np


day_4_input = namedtuple("day_4_input", ["random_numbers", "bingo_matrices"])


def get_input(matrix_length=5) -> day_4_input:
    with open("input", "r") as f:
        lines = f.readlines()

    random_numbers = get_random_numbers(lines[0])
    lines = lines[1:]

    boards = []
    for i in range(0, len(lines), matrix_length + 1):
        package = lines[i : i + matrix_length + 2]
        boards.append(make_board(package))

    return random_numbers, boards


def get_random_numbers(line) -> list:
    header = line.strip("\n")
    numbers = [int(number) for number in header.split(",")]
    return numbers


def make_board(lines: list[str], matrix_length=5) -> NDArray:
    numbers = (
        "".join(lines)  # join all lines into one long string
        .replace("\n", " ")  # remove line endings
        .replace("  ", " ")  # remove all double spaces
        .strip()
    )

    assert set(numbers) - set("0123456789 ") == set()
    board = np.array([int(n) for n in numbers.split(" ")])

    return board.reshape([matrix_length, matrix_length])


if __name__ == "__main__":
    print(get_input())
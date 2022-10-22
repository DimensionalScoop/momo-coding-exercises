import numpy as np
from numpy.typing import NDArray

import read


def get_winning_board(random_numbers, boards):
    calls = []
    for n in random_numbers:
        calls.append(n)
        for b in boards:
            if has_bingo(b, calls):
                return b, n


def has_bingo(board: NDArray, numbers: list):
    calls = np.isin(board, numbers)
    return has_complete_lines(calls) or has_complete_lines(calls.T)


def has_complete_lines(calls: NDArray):
    for line in calls:
        if line.all():
            return True
    return False


if __name__ == "__main__":
    random_numbers, boards = read.get_input()
    board, last_call = get_winning_board(random_numbers, boards)

    # sum of unmarked numbers
    last_call_idx = random_numbers.index(last_call) + 1
    calls = random_numbers[:last_call_idx]
    was_called = np.isin(board, calls)

    print(board[~was_called].sum() * last_call)

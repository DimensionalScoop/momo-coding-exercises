from dataclasses import replace
import numpy as np

def load():
    input = open("adventofcode21/momo_d4/input")

    input_numbers = input.readline().rsplit(",")
    input_numbers[-1] = input_numbers[-1].replace("\n", "")
    input_numbers = [int(i) for i in input_numbers]

    board_list = []
    board = []
    for line in input:
        if line is "\n":
            boards = np.array(board)
            board_list.append(boards)
            board.clear()
        else:
            board_line = line.split()
            board_line[-1] = board_line[-1].replace("\n", "")
            board_line = [int(i) for i in board_line]
            board.append(board_line)

    return input_numbers, board_list

def check_draw(number, board, check):
    x = np.nonzero(board == number)
    check[x] = 1

def check_win(check, c , w):
    lines = np.count_nonzero(check, axis=0) 
    rows = np.count_nonzero(check, axis=1)

    if w[c] == 1:
        return False

    if len(lines[lines == 5]) >= 1:
        w[c] = 1
        return True
    if len(rows[rows == 5]) >= 1:
        w[c] = 1
        return True

    return False


def calculate_score(board, check, number):
    print(np.sum(board[check == 0])*number)

    return 0


if __name__ == "__main__":
    input_numbers, board_list = load()

    check_list = []
    checks = np.zeros((5,5))
    for i in range(len(board_list)):
        check_list.append(checks.copy())

    w = np.zeros(len(board_list))
    c_list = range(len(board_list))
    for i in input_numbers:
        for board, check, c in zip(board_list, check_list, c_list):
            check_draw(i, board, check)
            if check_win(check, c, w):
                calculate_score(board, check, i)
                
            
from dataclasses import replace
import numpy as np

input = open("adventofcode21/momo_d4/input")

input_numbers = input.readline().rsplit(",")
input_numbers[-1] = input_numbers[-1].replace("\n", "")
input_numbers = [int(i) for i in input_numbers]


board_list = []
board = []
for line in input:
    if line is "\n":
        board_list.append(board)
        board.clear()
    else:
        board_line = line.split()
        board_line[-1] = board_line[-1].replace("\n", "")
        board_line = [int(i) for i in board_line]
        board.append(board_line)

print(board_list[-1])
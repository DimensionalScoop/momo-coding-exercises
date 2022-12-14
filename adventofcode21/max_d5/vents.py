import numpy as np


def add_vent(ocean, p1, p2, allow_diagonals=True):
    ocean = ocean.copy()
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2:
        if y2 < y1:
            y1, y2 = y2, y1
        ocean[x1, y1 : y2 + 1] += 1
    elif y1 == y2:
        if x2 < x1:
            x1, x2 = x2, x1
        ocean[x1 : x2 + 1, y1] += 1
    else:
        if allow_diagonals:
            x, y = x1, y1
            xdir = np.sign(x2 - x1)
            ydir = np.sign(y2 - y1)
            steps = np.abs(x2 - x1) + 1
            for _ in range(steps):
                ocean[x, y] += 1
                x += xdir
                y += ydir

    return ocean

def load_vent_lines(fname):
    with open(fname) as f:
        input_ = [l.replace("->", ",") for l in f.readlines()]

    points = np.genfromtxt(input_, delimiter=",", dtype="int32")
    start_points, end_points = points[:, :2], points[:, 2:]
    return start_points, end_points

def draw_ocean_floor(start_points, end_points):
    ocean_size = np.max([start_points, end_points]) + 1
    ocean = np.zeros([ocean_size] * 2)

    for p1, p2 in zip(start_points, end_points):
        ocean = add_vent(ocean, p1, p2, True)

    return ocean
    
def count_vent_crossings(ocean):
    return np.sum(ocean>1)


if __name__ == "__main__":
    start_points, end_points = load_vent_lines("input")
    ocean = draw_ocean_floor(start_points, end_points)
    n_crossings = count_vent_crossings(ocean)
    print(n_crossings)
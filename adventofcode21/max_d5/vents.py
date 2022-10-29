import numpy as np


def add_ortho_vent(ocean, p1, p2):
    ocean = ocean.copy()
    x1, y1 = p1
    x2, y2 = p2

    if x2 < x1:
        x1, x2 = x2, x1
    if y2 < y1:
        y1, y2 = y2, y1

    if x1 == x2:
        ocean[x1, y1 : y2 + 1] += 1
    elif y1 == y2:
        ocean[x1 : x2 + 1, y1] += 1
    else:  # diagonal
        pass
    return ocean


if __name__ == "__main__":
    with open("input") as f:
        input_ = [l.replace("->", ",") for l in f.readlines()]

    points = np.genfromtxt(input_, delimiter=",", dtype="int32")
    start_points, end_points = points[:, :2], points[:, 2:]

    ocean_size = np.max(points) + 1
    ocean = np.zeros([ocean_size] * 2)

    for p1, p2 in zip(start_points, end_points):
        ocean = add_ortho_vent(ocean, p1, p2)

    print((ocean > 1).sum())

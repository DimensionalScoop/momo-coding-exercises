import numpy as np


def load():
    with open("momo_d5/input") as input:
        cleanup = (line.replace("->", ",") for line in input)
        x1, y1, x2, y2 = np.genfromtxt(
            cleanup, delimiter=',', unpack=True, dtype=int)

    return x1, y1, x2, y2


def draw_vent(x1, y1, x2, y2, floor):
    if (x1 == x2):
        if y2 < y1:
            y1, y2 = y2, y1
        floor[x1, y1:y2+1] += 1
    elif (y1 == y2):
        if x2 < x1:
            x1, x2 = x2, x1
        floor[x1:x2+1, y1] += 1
    else:  # diagonal
        if x1 < x2:
            xrange = range(x1, x2+1)
        else:
            xrange = range(x1, x2-1, -1)
        if y1 < y2:
            yrange = range(y1, y2+1)
        else:
            yrange = range(y1, y2-1, -1)
        for x, y in zip(xrange, yrange):
            floor[x, y] += 1
    return None


def count_crossings(floor):
    return np.sum(floor >= 2)


if __name__ == "__main__":
    x1s, y1s, x2s, y2s = load()

    x_max = max(np.amax(x1s), np.amax(x2s))
    y_max = max(np.amax(y1s), np.amax(y2s))

    floor = np.zeros((x_max+1, y_max+1))

    for x1, y1, x2, y2 in zip(x1s, y1s, x2s, y2s):
        draw_vent(x1, y1, x2, y2, floor)

    print(count_crossings(floor))

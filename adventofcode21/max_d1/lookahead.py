with open("input") as f:
    depths = [int(line) for line in f.readlines()]

look_ahead = 3

increases = [True for d1, d2 in zip(depths, depths[look_ahead:]) if d1 < d2]
print(len(increases))
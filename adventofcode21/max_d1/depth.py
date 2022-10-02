with open("input") as f:
    depths = [int(line) for line in f.readlines()]

increases = [True for d1, d2 in zip(depths, depths[1:]) if d1 < d2]
print(len(increases))

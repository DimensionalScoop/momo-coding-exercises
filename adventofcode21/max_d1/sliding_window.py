with open("input") as f:
    depths = [int(line) for line in f.readlines()]

increases = 0
window_size = 3
look_ahead = 1
max_steps = len(depths) - window_size - look_ahead

for i in range(max_steps):
    window_a = depths[i : i + window_size]
    window_b = depths[i + look_ahead : i + look_ahead + window_size]

    if sum(window_b) > sum(window_a):
        increases += 1


print(increases)

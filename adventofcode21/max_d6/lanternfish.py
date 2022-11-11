import numpy as np

# index is age, value is number of fishies
count = np.zeros(9, "int64")

fishies = np.genfromtxt("input", "int32", delimiter=",")
ages, starting_counts = np.unique(fishies, return_counts=True)
for start_age, start_count in zip(ages, starting_counts):
    count[start_age] += start_count


def step():
    respawn = count[0]
    count[:-1] = count[1:]
    count[-1] = 0

    count[8] += respawn
    count[6] += respawn


for _ in range(256):
    step()

print(f"{count.sum():e}")

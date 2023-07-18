# %%
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

dt = 1e-3
v = 1
a = 10

initial_pos = np.array([[a, a], [a, -a], [-a, -a], [-a, a]])
sheep = initial_pos.copy()


def step():
    movement = []
    for this_sheep, next_sheep in zip(sheep, np.roll(sheep, 2)):
        xs = next_sheep[0] - this_sheep[0]
        ys = next_sheep[1] - this_sheep[1]
        angle = np.arctan2(ys, xs)
        dx = np.cos(angle) * v * dt
        dy = np.sin(angle) * v * dt
        movement.append([dx, dy])
    return np.asarray(movement)


sheep_pos_by_time = []
for i in tqdm(range(15000)):
    sheep_pos_by_time.append(sheep)
    sheep = sheep + step()
    if sheep[0, 0] < dt:
        break

sheep_pos_by_time = np.asarray(sheep_pos_by_time)

plt.scatter(*initial_pos.T)

for i in range(len(sheep)):
    plt.plot(*sheep_pos_by_time[:, i, :].T)

plt.gca().set_aspect('equal')
plt.show()
# %%

one_sheep = sheep_pos_by_time[:, 0, :]
radius = np.sqrt((one_sheep ** 2).sum(axis=1))
plt.plot(radius)
# %%

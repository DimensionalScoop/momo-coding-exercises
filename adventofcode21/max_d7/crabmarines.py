import numpy as np

pos = np.genfromtxt("input", "int32", delimiter=",")
optimal_pos = np.median(pos)

fuel_cost = [np.abs(pos - i).sum() for i in range(pos.min(), pos.max() + 1)]
print(min(fuel_cost), np.where(fuel_cost == min(fuel_cost)))

assert np.where(fuel_cost == min(fuel_cost)) == optimal_pos




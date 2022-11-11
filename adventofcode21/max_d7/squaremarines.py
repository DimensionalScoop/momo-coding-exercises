import numpy as np

pos = np.genfromtxt("input", "int32", delimiter=",")

def gauss_sum(n):
    n = np.abs(n)
    return (n**2 + n) // 2

optimal_pos = np.mean(pos)

fuel_cost = [
    sum(gauss_sum(pos - i)) 
    for i in range(pos.min(), pos.max() + 1)
]

print(min(fuel_cost), np.where(fuel_cost == min(fuel_cost)))

assert fuel_cost.index(min(fuel_cost)) == optimal_pos

import matplotlib.pyplot as plt

#plt.hist(pos,bins=int(np.sqrt(len(pos))))
#plt.plot(range(pos.min(), pos.max() + 1), fuel_cost)
#plt.show()


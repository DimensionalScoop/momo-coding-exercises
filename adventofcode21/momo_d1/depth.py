from gettext import npgettext


import numpy as np 

z = np.genfromtxt("adventofcode21/momo_d1/input")

sliding =[]
for r in range(np.size(z)-2):
    window = z[r:r+3]
    assert len(window) == 3, f"Should contain 3 elements, but got {window!r}"
    sliding.append(np.sum(window))

i = 0

for d1, d2 in zip(sliding, sliding[1:]):
    if d2 > d1: i+=1

print(i)


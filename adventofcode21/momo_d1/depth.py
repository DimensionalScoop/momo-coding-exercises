from gettext import npgettext


import numpy as np 

z = np.genfromtxt("adventofcode21/momo_d1/input")

i = 0

for d1, d2 in zip(z, z[1:]):
    if d2 > d1: i+=1

print(i)

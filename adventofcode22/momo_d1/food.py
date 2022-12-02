import numpy as np

with open("momo_d1/input") as file:
    lines = [line.rstrip() for line in file]

package = []
cal = 0

for l in lines:
    if l:
        cal += int(l)
    else:
        package.append(cal)
        cal = 0

total_top = 0

top = np.linspace(0 , 2, 3)
for i in top:
   total_top += package.pop(np.array(package).argmax())
   print(total_top)
   print(i)

print(total_top)
with open("adventofcode21/momo_d2/input") as file:
    f = [line.split() for line in file.readlines()]

x = 0
z = 0


for d in f:
    match d[0]:
        case 'up': z -= int(d[1])
        case 'down': z += int(d[1])
        case 'forward': x += int(d[1])

print(x*z)
        
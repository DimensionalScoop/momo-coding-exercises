with open("adventofcode21/momo_d2/input") as file:
    f = [line.split() for line in file.readlines()]

x = 0
z = 0


for cmd, number in f:
    number = int(number)
    match cmd:
        case 'up': z -= number
        case 'down': z += number
        case 'forward': x += number
        case _: raise ValueError()

print(x*z)
        
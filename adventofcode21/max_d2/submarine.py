with open("input") as f:
    lines = f.readlines()

horizontal = 0
depth = 0
aim = 0

for line in lines:
    cmd, number = line.split()
    steps = int(number)
    match cmd:
        case "forward":
            horizontal += steps
            depth += steps * aim
        case "down":
            aim += steps
        case "up":
            aim -= steps
        case _:
            raise NotImplementedError()

print(depth * horizontal)

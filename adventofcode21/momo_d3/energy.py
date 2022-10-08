with open("adventofcode21/momo_d3/input") as file:
    f = [line.strip('\n') for line in file.readlines()]

len_input = len(f[1])
anzahl_input = len(f)

gamma = str("")
epsilon = str("")

oxygen = f.copy()
co2 = f.copy()

for i in range(len_input):
    ones = 0
    for line in f: 
        if line[i] == "1": ones += 1
    
    if ones > (anzahl_input)/2:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    else: 
        gamma = gamma + "0"
        epsilon = epsilon + "1"
    
    if len(oxygen) > 1:
        ones = 0
        for line in oxygen:
             if line[i] == "1": ones += 1

        if ones >= len(oxygen)/2:
            oxygen = [elem for elem in oxygen if elem[i] == "1"]
        else:
            oxygen = [elem for elem in oxygen if elem[i] == "0"]

    if len(co2) > 1:
        ones = 0
        for line in co2:
             if line[i] == "1": ones += 1

        if ones >= len(co2)/2:
            co2 = [elem for elem in co2 if elem[i] == "0"]
        else:
            co2 = [elem for elem in co2 if elem[i] == "1"]

gamma = int(gamma, base = 2)
epsilon = int(epsilon, base = 2)
co2 = int(co2[0], base = 2)
oxygen = int(oxygen[0], base = 2 )

energy = gamma * epsilon 
life = oxygen * co2

print(energy)
print(life)

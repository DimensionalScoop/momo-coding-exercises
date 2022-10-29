import numpy as np


def generate_fishes(filename):
    input = open("momo_d6/"+filename, "r")
    fishes = [int(fish) for fish in input.readline().strip("\n").split(",")]

    cycle = np.array(range(9), dtype="int64")

    for i in range(9):
        cycle[i] = fishes.count(i)

    return cycle

def reproduction_cycle(cycle : np.ndarray):
    new_fishes = cycle[0]
    cycle[:-1] = cycle[1:]

    cycle[-1] = new_fishes
    cycle[6] += new_fishes

    return cycle

def count_fish(cycle: np.ndarray):
    return np.sum(cycle)

if __name__ == "__main__":
    CYCLES = 256
    cycle = generate_fishes("input") 
    print(cycle)

    for i in range(CYCLES):
        cycle = reproduction_cycle(cycle)
        print(cycle)

    amount_fishes = count_fish(cycle)
    print(amount_fishes)
    

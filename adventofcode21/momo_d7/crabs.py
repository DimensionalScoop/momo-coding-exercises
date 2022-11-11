import numpy as np

def load():
    positions = np.genfromtxt("momo_d7/input", delimiter=",", dtype=int)
    return positions

def find_optimal_position(positions):
    best = 488520*10000
    best_position = 0
    for i in range(positions.max()):
        fuel = 0
        for pos in positions:
            difference = np.abs(pos - i)
            move = np.sum(range(difference+1))
            fuel += move

        if fuel < best:
            best = fuel
            best_position = i
    return best, best_position

if __name__ == "__main__":
    positions = load()
    
    solution, solution_position = find_optimal_position(positions)

    print(solution)
def load():
    input = open("momo_d8/input")
    values = [line.strip("\n").split(" | ") for line in input.readlines()]
    
    signal = []
    output = []
    for val in values:
        signal.append(val[0])
        output.append(val[1])

    return signal, output


def split_output(output):
    out = []
    for line in output:
        strings = line.split()
        for s in strings:
            out.append(s)
    return out

def count_numbers(out):
    counts = 0

    for s in out:
        lenght = len(s)
        if lenght == 2 or lenght == 3 or lenght == 4 or lenght == 7:
            counts += 1

    return counts

if __name__ == "__main__":
    signal, output = load()
    out = split_output(output)
    counts = count_numbers(out)
    print(counts)
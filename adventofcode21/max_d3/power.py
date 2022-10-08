from typing import Iterable
import numpy as np


def iter_as_binary_number(a: Iterable) -> int:
    a = np.array(a).flatten()
    chars = [str(i) for i in a]
    string = "".join(chars)
    number = int(string, base=2)
    return number


def load() -> np.ndarray:
    with open("input") as file:
        chars = [
            [int(c) for c in line if c in ("0", "1")]
            for line in file.readlines()
        ]
        binary = np.array(chars, dtype="bool")
    return binary


if __name__ == "__main__":
    binary = load()

    gamma = np.round(binary.mean(axis=0)).astype("int")
    epsilon = 1 - gamma
    assert (gamma + epsilon).all()

    gamma = iter_as_binary_number(gamma)
    epsilon = iter_as_binary_number(epsilon)

    print(gamma * epsilon)

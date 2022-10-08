from typing import Iterable
import numpy as np

from power import load


def order_by_occurrences(a: Iterable) -> list:
    """
    Returns a list of all unique symbols in `a`, ordered from least to most
    frequently occurring in `a`.

    >>> order_by_occurrences([10,3,22,22,3,3,3])
    [10, 22, 3]
    """
    entries, count = np.unique(a, return_counts=True)
    freq = entries[np.argsort(count)]
    return freq.tolist()


def o2_criterion(numbers: Iterable) -> int:
    """
    >>> o2_criterion([1, 1, 0, 0])
    1
    >>> o2_criterion([0, 0, 0, 1])
    0
    """
    most_common = order_by_occurrences(numbers)[::-1]
    return_value = most_common[0]

    if most_common[0] == most_common[1]:
        return_value = 1
    return return_value


def co2_criterion(numbers: Iterable) -> int:
    """
    >>> co2_criterion([1, 1, 0, 0])
    0
    >>> co2_criterion([0, 0, 0, 1])
    1
    """
    least_common = order_by_occurrences(numbers)
    return_value = least_common[0]

    if least_common[0] == least_common[1]:
        return_value = 0
    return return_value


def filter_number(criterion, binary):
    valid = binary
    nth_bit = 0
    while len(valid) > 1:
        numbers = valid[:, nth_bit]
        keep = criterion(numbers)
        filter_ = valid[:, nth_bit] == keep
        valid = valid[filter_]

        nth_bit += 1
    return valid


def binary_array_to_int(a) -> int:
    a = "".join(str(i) for i in a.flatten())
    a = int(a, base=2)
    return a


if __name__ == "__main__":
    binary = load().astype("int")
    o2_array = filter_number(o2_criterion, binary)
    o2 = binary_array_to_int(o2_array)

    co2_array = filter_number(co2_criterion, binary)
    co2 = binary_array_to_int(co2_array)

    print(o2 * co2)

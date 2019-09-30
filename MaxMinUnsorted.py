def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints is None or len(ints) == 0:
        return None, None

    max = ints[0]
    min = ints[0]

    for num in ints:
        if num < min:
            min = num
        if num > max:
            max = num

    return min, max


# Example Test Case of Ten Integers

import random

l = [i for i in range(1, 1000)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((1, 999) == get_min_max(l)) else "Fail")

l = [i for i in range(100, 1000)]  # a list containing 0 - 9

print("Pass" if ((100, 999) == get_min_max(l)) else "Fail")

print("Pass" if ((None, None) == get_min_max(list())) else "Fail")

print("Pass" if ((None, None) == get_min_max(None)) else "Fail")
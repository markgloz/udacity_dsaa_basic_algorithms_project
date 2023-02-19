def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints or None in ints:
        return (None, None)
    min = ints[0]
    max = ints[0]
    for int in ints:
        if int < min:
            min = int
        if int > max:
            max = int
    return (min, max)

# Supplied test
## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Test 1 - Normal use case
print(get_min_max([8, 4, 2, 1, 5, 7, 3, 918, 348, 2, 90, 328])) # (1, 918)

# Test 3 - Null value
print(get_min_max([None])) # (None, None)

# Test 4 - Empty value
print(get_min_max([])) # (None, None)

# Test 5 - Large value
print(get_min_max([940330, -2839392, 3032, 292819, -4930, 299292992929, 38, 394, 383829, -382193])) # (-2839392, 299292992929)
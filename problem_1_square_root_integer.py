def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None or number < 0:
        return None
    num = 0
    while number >= num * num:
        squared = num * num
        if number == squared:
            return num
        num += 1
    return num - 1

# Supplied tests
print ("Pass" if  (3 == sqrt(9)) else "Fail") # Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail") # Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail") # Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail") # Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail") # Pass

# Test 1 - Normal
print(sqrt(81)) # 9

# Test 2 - Negative value
print(sqrt(-1)) # None

# Test 3 - Null value
print(sqrt(None)) # None

# Test 5 - Large value
print(sqrt(9.5 ** 12.2)) # 920691
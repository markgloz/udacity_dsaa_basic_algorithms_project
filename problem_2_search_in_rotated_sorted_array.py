def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not input_list or len(input_list) == 1 and None in input_list:
        return -1
    return rotated_array_search_recursive(input_list, number, 0, len(input_list) - 1)

def rotated_array_search_recursive(input_list, number, start, end):
    mid = start + ((end - start) // 2)
    # Base case - element found
    if number == input_list[mid]:
        return mid
    # Base case - element not found
    if start >= end:
        return -1
    if input_list[mid - 1] >= input_list[start]: # Then we know this half does not contain rotation
        if input_list[start] <= number <= input_list[mid - 1]:
            return rotated_array_search_recursive(input_list, number, start, mid - 1)
        else:
            return rotated_array_search_recursive(input_list, number, mid + 1, end)
    else: # Otherwise this half does not contain rotation
        if input_list[mid + 1] <= number <= input_list[end]:
            return rotated_array_search_recursive(input_list, number, mid + 1, end)
        else:
            return rotated_array_search_recursive(input_list, number, start, mid - 1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Supplied tests
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) # Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8]) # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1]) # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10]) # Pass

# Test 1 - Sorted rotated array with non-equal spacing between values
print(rotated_array_search([48, 50, 80, 93, 95, 20, 34, 47], 47)) # 7

# Test 2 - Negative value
print(rotated_array_search([-4, -2, -1, 0, -40, -24, -11, -7], -2)) # 1

# Test 3 - Null value
print(rotated_array_search(None, 5)) # -1
print(rotated_array_search([None], 5)) # -1

# Test 4 - Empty value
print(rotated_array_search([], 5)) # -1

# Test 5 - Large value
print(rotated_array_search([9000, 50000, 100000, 3000, 4830, 5920, 7402, 7404, 7800, 8999], 5920)) # 5
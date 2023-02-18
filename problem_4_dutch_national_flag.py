def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    index = 0
    next_index_0 = 0
    next_index_2 = len(input_list) - 1
    for _ in range(len(input_list)):
        if input_list[index] == 0:
            input_list[index], input_list[next_index_0] = input_list[next_index_0], input_list[index]
            next_index_0 += 1
            index += 1
        elif input_list[index] == 2:
            input_list[index], input_list[next_index_2] = input_list[next_index_2], input_list[index]
            next_index_2 -= 1
        else:
            index += 1
    return

def test_function(test_case):
    answer = sorted(test_case)
    sort_012(test_case)
    print(test_case)
    if test_case == answer:
        print("Pass")
    else:
        print("Fail")

# Supplied tests
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
 # [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
 # Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
# Pass

# Test 1 - Normal use case
test_array = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
sort_012(test_array)
print(test_array) # [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]

# Test 2 - Empty value
test_array = []
sort_012(test_array)
print(test_array) # []

# Test 3 - Large array
test_array = [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 0, 1, 0, 1, 2, 2, 2, 1, 1, 2, 2, 0, 0, 0, 1, 2, 1, 2, 0]
sort_012(test_array)
print(test_array) # [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
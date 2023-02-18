def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    quicksort(input_list) # O(n logn) time complexity; O(log n) space complexity due to recursion depth
    number_1 = ''
    number_2 = ''
    for index in range(len(input_list) - 1, -1, -1):
        if not input_list[index]:
            continue
        if index % 2 == 0: # Even index
            number_1 += str(input_list[index])
        else: # Odd index
            number_2 += str(input_list[index])
    if not number_1 or not number_2:
        return []
    return [int(number_1), int(number_2)]

def quicksort(arr):
    quicksort_recursive(arr, 0, len(arr) - 1)

def quicksort_recursive(arr, start, end):
    if start >= end: # Base case
        return
    pivot = sort_pivot(arr, start, end)
    quicksort_recursive(arr, start, pivot - 1)
    quicksort_recursive(arr, pivot + 1, end)

def sort_pivot(arr, start, end):
    pivot = end
    pivot_value = arr[pivot]
    left = start

    if not arr[pivot]:
        return pivot
    
    while pivot > left:
        left_value = arr[left]
        if left_value and left_value <= pivot_value:
            left += 1
            continue
        arr[left] = arr[pivot - 1]
        arr[pivot - 1] = pivot_value
        arr[pivot] = left_value
        pivot -= 1
    
    return pivot


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Provided tests
test_function([[1, 2, 3, 4, 5], [542, 31]]) # Pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]]) # Pass

# Test 1 - Normal use case
test_array = [5, 3, 9, 5, 3, 1, 2]
solution = rearrange_digits(test_array)
print(solution) # [9531, 532]

# Test 2 - Lots of large duplicate elements
test_array = [9, 9, 9, 8, 8, 8, 4, 4, 2, 2, 7, 3]
solution = rearrange_digits(test_array)
print(solution) # [988432, 998742]

# Test 3 - Null value
test_array = [None]
solution = rearrange_digits(test_array)
print(solution) # []

test_array = [2, 4, 1, 3, None, 6, None]
solution = rearrange_digits(test_array)
print(solution) # [631, 42]

# Test 4 - Empty value
test_array = []
solution = rearrange_digits(test_array)
print(solution) # []

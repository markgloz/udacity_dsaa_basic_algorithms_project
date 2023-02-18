def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return rotated_array_search_recursive(input_list, number, 0, len(input_list) - 1)
    
def rotated_array_search_recursive(input_list, number, start, end):
    mid = start + ((end - start) // 2)
    if number == input_list[mid]:
        return mid
    elif input_list[start] <= number <= input_list[mid - 1] or input_list[mid - 1] <= number <= input_list[start]:
        return rotated_array_search_recursive(input_list, number, start, mid - 1)
    elif input_list[mid + 1] <= number <= input_list[end] or input_list[end] <= number <= input_list[mid + 1]:
        return rotated_array_search_recursive(input_list, number, mid + 1, end)
    else:
        return -1

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

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
def rotated_array_search_recursive(input_list, number, carry):

    if input_list is None or number is None or len(input_list) == 0:
        return -1

    mid_index = len(input_list) // 2
    if input_list[mid_index] == number:
        return mid_index + carry
    elif input_list[0] == number:
        return 0 + carry
    elif input_list[len(input_list) - 1] == number:
        return len(input_list) - 1 + carry

    if len(input_list) <= 3:
        return -1

    sorted_list = None
    unsorted_list = None
    sorted_first = False
    if input_list[0] < input_list[mid_index]:
        sorted_list = input_list[:mid_index + 1]
        unsorted_list = input_list[mid_index + 1:]
        sorted_first = True
    else:
        unsorted_list = input_list[:mid_index + 1]
        sorted_list = input_list[mid_index + 1:]

    #print("sorted {0}".format(sorted_list))
    #print("unsorted {0}".format(unsorted_list))

    if sorted_list[0] >= number >= sorted_list[mid_index]:
        #print("sorted search")
        pcarry = carry
        if not sorted_first:
            pcarry += mid_index+1
        return rotated_array_search_recursive(sorted_list, number, pcarry)
    else:
        #print("unsorted search")
        pcarry = carry
        if sorted_first:
            pcarry += mid_index+1
        return rotated_array_search_recursive(unsorted_list, number, pcarry)


def rotated_array_search(input_list, number):
    '1)split array into two '
    '2)check for the bounds in each two and identify which one is the sorted or unsorted array'
    '3)if the target is within bounds of the sorted array, just split it in two and search for it '
    '4)if the target is within unsorted, repeat'
    return rotated_array_search_recursive(input_list, number, 0)


def linear_search(input_list, number):
    if input_list is None:
        return -1

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
        print(rotated_array_search(input_list, number))


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], 10])
test_function([[10], 10])
test_function([None, 10])

test_function([[7, 12, 16, 18, 19, 23, 1, 3, 4, 6], 10])
test_function([[7, 12, 16, 18, 19, 23, 1, 3, 4, 6], 7])
test_function([[7, 12, 16, 18, 19, 23, 1, 3, 4, 6], 4])
test_function([[7, 12, 16, 18, 19, 23, 1, 3, 4, 6], 2])
test_function([[7, 12, 16, 18, 19, 23, 1, 3, 4, 6], 20])

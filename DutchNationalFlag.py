def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list is None:
        print("Sort impossible")
        return input_list

    zero_index = 0
    two_index = len(input_list) - 1
    index = 0

    while index <= two_index:
        if input_list[index] == 1:
            index += 1
            continue
        if input_list[index] == 2:
            two_ind_val = input_list[two_index]
            if two_ind_val == 2:
                two_index += -1
                continue
            elif two_ind_val == 1:
                input_list[index] = 1
                input_list[two_index] = 2
                two_index += -1
            else:
                input_list[zero_index] = 0
                if index != zero_index:
                    input_list[index] = 1
                input_list[two_index] = 2
                two_index += -1
                zero_index += 1
        else:
            input_list[index] = 1
            input_list[zero_index] = 0
            zero_index += 1
        index += 1

    return input_list


def test_function(test_case):

    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print(sorted_array)
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 0, 1, 2, 1, 1, 1, 1, 0, 2])
test_function([2, 1, 2, 1, 2])
test_function([0, 0, 2, 0, 2])
test_function([])
#test_function(None)

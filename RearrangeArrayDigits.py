import copy


def rearrange_digits(input_list):

    if len(input_list) == 0:
        return list()

    return rearrange_digits_recursive(input_list, list(), 0, len(input_list)-1)


def rearrange_digits_recursive(input_list, helper, start, end):

    if start < end:
        middle = (start+end)//2
        rearrange_digits_recursive(input_list, helper, start, middle )
        rearrange_digits_recursive(input_list, helper, middle+1, end)
        if (start + end) == len(input_list) - 1:
            input_list = merge_into_two(input_list, helper, start, middle, end)
        else:
            input_list = merge(input_list, helper, start, middle, end)
        return input_list


def merge_into_two(input_list, helper, start, middle, end):

    helper = copy.deepcopy(input_list)

    current = start
    left_index = start
    right_index = middle+1
    even = 0
    odd = 0
    while left_index <= middle and right_index <= end:
        if helper[left_index] <= helper[right_index]:
            if current%2 == 0:
                even = even * 10 + helper[right_index]
            else:
                odd = odd * 10 + helper[right_index]
            right_index += 1
            #print("right value of {0} is {1}".format(current, input_list[current]))
        else:
            if current%2 == 0:
                even = even * 10 + helper[left_index]
            else:
                odd = odd * 10 + helper[left_index]
            left_index +=1
            #print("left value of {0} is {1}".format(current, input_list[current]))
        current += 1

    rem = middle-left_index
    ind = 0
    while ind <= rem:
        #input_list[current+ind] = helper[left_index+ind]
        if (current+ind) % 2 == 0:
            even = even * 10 + helper[left_index+ind]
        else:
            odd = odd * 10 + helper[left_index+ind]
        #print("rem==value of {0} is {1}".format(current+ind, input_list[current+ind]))
        ind +=1

    r_list = list()
    r_list.append(even)
    r_list.append(odd)
    return r_list


def merge(input_list, helper, start, middle, end):

    helper = copy.deepcopy(input_list)

    current = start
    left_index = start
    right_index = middle+1

    while left_index <= middle and right_index <= end:
        if helper[left_index] <= helper[right_index]:
            input_list[current] = helper[right_index]
            right_index += 1
            #print("right value of {0} is {1}".format(current, input_list[current]))
        else:
            input_list[current] = helper[left_index]
            left_index +=1
            #print("left value of {0} is {1}".format(current, input_list[current]))
        current+=1

    rem = middle-left_index
    ind = 0
    while ind <= rem:
        input_list[current+ind] = helper[left_index+ind]
        #print("rem==value of {0} is {1}".format(current+ind, input_list[current+ind]))
        ind +=1

    return input_list


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print(output)
        print("Fail")



test_function([[1, 2], [2, 1]])

test_function([[1, 2, 3, 4, 5], [531, 42]])

test_function([[1, 2], [2, 1]])

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

test_function([[], []])

test_function([[1, 2, 4, 5, 8, 9], [952, 841]])



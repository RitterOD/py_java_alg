import random

def shift_binary_search(data, val):
    step = len(data) // 2
    ind = len(data) // 2 + len(data) % 2
    is_find = False
    while step != 0:
        if data[ind] == val:
            is_find = True
            break
        elif data[ind] > val:
            ind = (ind + len(data) - step) % len(data)
        else:
            ind = (ind + step) % len(data)
        step = step // 2
    if is_find:
        return ind
    else:
        return -1

def produce_test_data(min_size, max_size, min_val, max_val):
    lst_size = random.randint(min_size, max_size)
    lst = [random.randint(min_val, max_val) for _ in range(lst_size)]
    lst.sort()
    splt_ind = random.randint(1, lst_size - 1)
    #print(splt_ind)
    #print(lst)
    left_side = lst[0:splt_ind]
    right_side = lst[splt_ind:]
    lst = right_side + left_side
    return lst

def perform_test(data):
    search_ind = random.randint(0, len(data) - 1)
    search_val = data[search_ind]
    solution = shift_binary_search(data, search_val)
    if data[solution] != data[search_ind]:
        return False
    else:
        return True


def perform_negative_test(data, min_val, max_val):
    check_set = set(data)
    check_val = random.randint(min_val, max_val)
    while check_val in check_set:
        check_val = random.randint(min_val, max_val)
    rv = shift_binary_search(data, check_val)
    if rv == -1:
        return True
    else:
        return False

if __name__ == '__main__':
    print('shift binary search')
    random.seed()
    for ind in range(0, 5):
        test_data = produce_test_data(10, 50, 90, 1000)
        rv = perform_test(test_data)
        if not rv:
            print('Postive test fail ', ind)
        rv = perform_negative_test(test_data, 90, 1000)
        if not rv:
            print('Negative test fail', ind)
        if ind % 100 == 0:
            print('iter = ', ind)
    print('Finish')
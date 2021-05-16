import random

def find_broad(data):
    left = 0
    right = len(data)
    while True:
        mid = (left + right) // 2
        if data[mid] < data[left]:
            right = mid
        else:
            left = mid
        if right - left == 0 or right - left == 1:
            rv = (right, left)
            break
    return rv


def shift_binary_search(data, val):
    rv = -1
    left, right = find_broad(data)
    try:
        while True:
            if left == right:
                if data[left] == val:
                    rv = left
                break
            elif right - left == 1 or (right == 0 and left == len(data) - 1):
                if data[left] == val:
                    rv = left
                if data[right] == val:
                    rv = right
                break
            if right < left:
                mid = ((len(data) - left + right +1) // 2 + left) % len(data)
                if mid >= len(data):
                    print('overflow')
            else:
                mid = (left + right) // 2
            if data[mid] == val:
                rv = mid
                break
            elif data[mid] > val:
                right = mid - 1
                if right < 0:
                    right = len(data) - 1
            else:
                left = (mid + 1) % len(data)
    except Exception as e:
        print(e)

    return rv

def produce_test_data(min_size, max_size, min_val, max_val):
    lst_size = random.randint(min_size, max_size)
    lst = [random.randint(min_val, max_val) for _ in range(lst_size)]
    lst.sort()
    splt_ind = random.randint(1, lst_size - 1)

    left_side = lst[0:splt_ind]
    right_side = lst[splt_ind:]
    lst = right_side + left_side

    broad = find_broad(lst)
    if lst[broad[0]] > lst[broad[1]]:
        print('error')
        print(splt_ind)
        print(lst)
        print(broad)

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
    for ind in range(0, 1000):
        test_data = produce_test_data(10, 20, 90, 1000)
        rv = perform_test(test_data)
        if not rv:
            print('Postive test fail ', ind)
        rv = perform_negative_test(test_data, 90, 1000)
        if not rv:
            print('Negative test fail', ind)
        if ind % 100 == 0:
            print('iter = ', ind)
    print('Finish')
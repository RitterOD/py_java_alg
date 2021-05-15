import random



def binarySearch(arr, x, left, right):
    rv = -1
    left = 0
    right = len(arr)
    while True:
        if right <= left: # промежуток пуст
            break
        # промежуток не пуст
        mid = (left + right) // 2
        if arr[mid] == x: # центральный элемент — искомый
            rv = mid
            break
        elif x < arr[mid]: # искомый элемент меньше центрального
                       # значит следует искать в левой половине
            right = mid
        else: # иначе следует искать в правой половине
            left = mid + 1
    return rv


def produce_test_data(min_size, max_size, min_val, max_val):
    lst_size = random.randint(min_size, max_size)
    lst = [random.randint(min_val, max_val) for _ in range(lst_size)]
    lst.sort()
    return lst



if __name__ == '__main__':
    print('shift binary search')
    random.seed()

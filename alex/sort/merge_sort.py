from array import array


def merge(arr: list, left: int, mid:int, right: int) -> array:
    tmp_arr = [0] * (right - left)
    print('left =', arr[left:mid])
    print('right =', arr[mid:right])
    cur_ind = 0
    cur_left = left
    cur_right = mid
    while cur_ind != (right - left):
        if cur_left != mid and cur_right != right:
            if arr[cur_left] < arr[cur_right]:
                tmp_arr[cur_ind] = arr[cur_left]
                cur_left += 1
            else:
                tmp_arr[cur_ind] = arr[cur_right]
                cur_right += 1
        elif cur_left == mid:
            tmp_arr[cur_ind] = arr[cur_right]
            cur_right += 1
        else:
            tmp_arr[cur_ind] = arr[cur_left]
            cur_left += 1
        cur_ind += 1
    print(tmp_arr)
    for ind in range(left, right):
        arr[ind] = tmp_arr[ind - left]
    return arr


def merge_sort(arr: list, left: int, right: int) -> None:
    if right - left == 1 or right == left:
        return arr
    else:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        merge(arr, left, mid, right)


if __name__ == '__main__':
    print('Merge sort')
    tst = [4, 5, 3, 0, 1, 2]
    #tst = [4, 5, 3]
    print('before =', tst)
    merge_sort(tst, 0, len(tst))
    print('after =', tst)
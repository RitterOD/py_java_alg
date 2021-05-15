from array import array


def merge(arr: list, left: int, mid:int, right: int) -> array:
    cur_sort = left
    cur_left = left
    cur_right = mid
    while cur_sort != right:
        if arr[cur_left] <= arr[cur_right]:
            cur_sort +=1
            cur_left +=1
        else:
            tmp = arr[cur_left]
            arr[cur_left] = arr[cur_right]
            arr[cur_right] = tmp
    return arr


def merge_sort(arr: list, left: int, right: int) -> None:
    if right - left == 1 or right == left:
        return arr
    else:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


if __name__ == '__main__':
    print('Merge sort')
    tst = [4, 5, 3, 0, 1, 2]
    print('before =', tst)
    merge_sort(tst, 0, len(tst))
    print('after =', tst)
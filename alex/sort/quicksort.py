
def partition_quciksort(ar, l, r):
    pivot = ar[r - 1]
    cur_less_ind = l - 1
    for ind in range(l, r - 1):
        if ar[ind] <= pivot:
            cur_less_ind += 1
            tmp = ar[ind]
            ar[ind] = ar[cur_less_ind]
            ar[cur_less_ind] = tmp
    cur_less_ind += 1
    tmp = ar[r - 1]
    ar[r - 1] = ar[cur_less_ind]
    ar[cur_less_ind] = tmp
    return cur_less_ind


def quicsort_rec(ar, l, r):
    if l < r:
        q = partition_quciksort(ar, l, r)
        quicsort_rec(ar, l, q)
        quicsort_rec(ar, q + 1, r)
    pass


tst_data = [2, 4, 1, 0, 3, 8, -5, 5, 10, -3]

if __name__ == '__main__':
    print('example of quicksort')
    print('Before sort')
    print(tst_data)
    quicsort_rec(tst_data, 0, len(tst_data))
    print('After sort\n')
    print(tst_data)
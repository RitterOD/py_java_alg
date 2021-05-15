
tst = [[15, 56, 2], [1, 783, 2]]
ans = [56215, 78321]


def cmp_number(a, b):
    dig_a = 0
    if a // 100 != 0:
        dig_a = 3
    elif a // 10 != 0:
        dig_a = 2
    else:
        dig_a = 1
    if b // 100 != 0:
        dig_b = 3
    elif b // 10 != 0:
        dig_b = 2
    else:
        dig_b = 1
    if dig_a == dig_b:
        return a <= b
    elif dig_a > dig_b:
        dif = dig_a - dig_b
        b = b * (10 ** dif) + (10 ** dif) - 1
        return a <= b
    else:
        dif = dig_b - dig_a
        a = a * (10 ** dif) + (10 ** dif) - 1
        return a <= b


def partition_quciksort(ar, l, r):
    pivot = ar[r - 1]
    cur_less_ind = l - 1
    for ind in range(l, r - 2):
        if cmp_number(ar[ind], pivot):
        #if ar[ind] <= pivot:
            cur_less_ind += 1
            tmp = ar[ind]
            ar[ind] = ar[cur_less_ind]
            ar[cur_less_ind] = tmp
    cur_less_ind += 1
    tmp = ar[r - 1]
    ar[r - 1] = ar[cur_less_ind]
    ar[cur_less_ind] = tmp
    return cur_less_ind


def spec_quicsort_rec(ar, l, r):
    if l < r:
        q = partition_quciksort(ar, l, r)
        spec_quicsort_rec(ar, l, q)
        spec_quicsort_rec(ar, q + 1, r)
    pass



def solution(arr):
    spec_quicsort_rec(arr, 0, len(arr))
    print(arr)
    rv = ""
    for ind in range(len(arr) - 1, -1, -1):
        rv += str(arr[ind])
    return int(rv)


if __name__ == '__main__':
    print('Big num')
    for ind in range(len(tst)):
        sol = solution(tst[ind])
        if sol != ans[ind]:
            print('Error in case', ind)
        else:
            print('Ok in case = ', ind)
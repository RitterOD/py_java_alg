# https://www.hackerrank.com/challenges/equal/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def calc_op(min_val, max_val):
    cnt = 0
    difference = abs(max_val - min_val)
    cnt += difference // 5
    difference %= 5

    cnt += difference // 2
    difference %= 2

    cnt += difference
    return cnt

def equal(arr):
    min_val = arr[0]
    min_ind = 0
    arr.sort(reverse=True)
    for ind in range(len(arr)):
        if min_val > arr[ind]:
            min_val = arr[ind]
            min_ind = ind
    cnt_op = 0
    for ind in range(len(arr)):
        max_val = arr[0]
        max_ind = 0
        for ind in range(len(arr)):
            if max_val < arr[ind]:
                max_val = arr[ind]
                max_ind = ind
        cnt_op += calc_op(arr[min_ind], arr[max_ind])
        arr[max_ind] = arr[min_ind]
    return cnt_op

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
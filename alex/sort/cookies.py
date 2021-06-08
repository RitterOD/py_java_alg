

def solve(cookies, pref):
    cookies.sort()
    pref.sort()
    cur_cookies = 0
    cur_pref = 0
    rv = 0
    while cur_cookies != len(cookies) and cur_pref != len(pref):
        if cookies[cur_cookies] <= pref[cur_pref]:
            cur_cookies += 1
            cur_pref += 1
            rv += 1
        else:
            cur_cookies += 1
    return rv


if __name__ == '__main__':
    print(solve([1, 2], [2, 1, 3]))
    print(solve([2, 1, 3], [1, 1]))
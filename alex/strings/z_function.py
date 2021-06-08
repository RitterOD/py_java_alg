
def z_fun(src):
    z = [0] * len(src)
    z[0] = len(src)
    left = 0
    right = 0
    for ind in range(1, len(src)):
        if left < ind < right:
            if ind + z[ind - left] <= right:
                z[ind] = z[ind - left]
            else:
                st_ind = ind - left
                sub_ind = right + 1
                z[ind] = right - ind
                while True:
                    if len(src) <= sub_ind:
                        break
                    elif src[st_ind] == src[sub_ind]:
                        st_ind += 1
                        sub_ind += 1
                        z[ind] += 1
                    else:
                        break
                left = ind
                right = sub_ind - 1
        else:
            st_ind = 0
            sub_ind = ind
            while True:
                if src[st_ind] == src[sub_ind]:
                    st_ind += 1
                    sub_ind += 1
                else:
                    break
                if sub_ind >= len(src):
                    break
            z[ind] = st_ind
            left = ind
            right = left + st_ind
        pass
    return z

def z_fun_wiki_imp(s):
    z = [0] * len(s)
    z[0] = len(s)
    left, right = 0, 0
    for i in range(1, len(s)):
        z[i] = max(0, min(z[i - left], right - i))
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


def check_result(z0, z1):
    if len(z0) != len(z1):
        return -1
    else:
        rv = 0
        for ind in range(len(z0)):
            if z0[ind] != z1[ind]:
                rv = -1
                break;
        return rv

tst1 = 'abvabvabv'

tst = ['a', 'aa', 'aaa', 'aaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaa']
#tst = ['aaaa', 'aaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaa']


def complex_test(data):
    for src in data:
        z0 = z_fun(src)
        z1 = z_fun_wiki_imp(src)
        rv = check_result(z0, z1)
        print('\n------------------------------')
        print(src)
        if rv != 0:
            print('error')
            print('z_fun =', z0)
            print('z_fun_wiki_imp =', z1)
        else:
            print('z_fun =', z0)
            print('test passed')


if __name__ == '__main__':
    z0 = z_fun(tst1)
    z1 = z_fun_wiki_imp(tst1)
    rv = check_result(z0, z1)
    if rv != 0:
        print('error')
        print('z_fun =', z0)
        print('z_fun_wiki_imp =', z1)
    else:
        print('z_fun =', z0)
        print('test passed')
    print('Start complex test')
    complex_test(tst)
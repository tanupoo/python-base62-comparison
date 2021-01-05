"""
 answered Mar 30 '10 at 23:58
 Wolph
"""
import string
# Remove the `_@` below for base62, now it has 64 characters
BASE_LIST = string.digits + string.ascii_letters + '_@'
BASE_DICT = dict((c, i) for i, c in enumerate(BASE_LIST))

def base_decode(string, reverse_base=BASE_DICT):
    length = len(reverse_base)
    ret = 0
    for i, c in enumerate(string[::-1]):
        ret += (length ** i) * reverse_base[c]

    return ret

def base_encode(integer, base=BASE_LIST):
    if integer == 0:
        return base[0]

    length = len(base)
    ret = ''
    while integer != 0:
        ret = base[integer % length] + ret
        integer //= length

    return ret

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        import timeit
        params = [
                ("rand128.dmp", 20000),
                ("rand256.dmp", 10000),
                ("rand512.dmp", 5000),
                ("rand1024.dmp", 2000),
                 ]
        func = "base_encode"
        for fname,nb_try in params:
            result = timeit.timeit(
                setup=f'''
from __main__ import {func}
buf = open("{fname}", "rb").read()
num = int.from_bytes(buf, "big")
                ''',
                stmt=f'''
e = {func}(num)
                ''',
                number=nb_try
            )
            print(fname, result)
    elif len(sys.argv) == 2:
        buf = open(sys.argv[1], "rb").read()
        num = int.from_bytes(buf, "big")
        e = base_encode(num)
        print(e)
    elif len(sys.argv) == 3:
        buf = open(sys.argv[1], "rb").read()
        num = int.from_bytes(buf, "big")
        e = base_encode(num)
        d = base_decode(e)
        print(d)
        print(num == d)

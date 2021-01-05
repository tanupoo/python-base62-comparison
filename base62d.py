"""
 answered Sep 26 '19 at 5:19
 kayleeFrye_onDeck
"""

#modified from Dr. Zhihua Lai's original on GitHub
from math import floor
#base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
base = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';

b = 62;
def toBase10(b62: str) -> int:
    limit = len(b62)
    res = 0
    for i in range(limit):
        res = b * res + base.find(b62[i])
    return res
def toBase62(b10: int) -> str:
    if b <= 0 or b > 62:
        return 0
    r = b10 % b
    res = base[r];
    q = floor(b10 / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res

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
        func = "toBase62"
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
        e = toBase62(num)
        print(e)
    elif len(sys.argv) == 3:
        buf = open(sys.argv[1], "rb").read()
        num = int.from_bytes(buf, "big")
        e = toBase62(num)
        d = toBase10(e)
        print(d)
        print(num == d)

"""
 answered May 6 '20 at 22:48
 melvil james
"""

#BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def encode_base62(num):
    s = ""
    while num>0:
      num,r = divmod(num,62)
      s = BASE62[r]+s
    return s


def decode_base62(num):
   x,s = 1,0
   for i in range(len(num)-1,-1,-1):
      s = int(BASE62.index(num[i])) *x + s
      x*=62
   return s

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
        func = "encode_base62"
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
        e = encode_base62(num)
        print(e)
    elif len(sys.argv) == 3:
        buf = open(sys.argv[1], "rb").read()
        num = int.from_bytes(buf, "big")
        e = encode_base62(num)
        d = decode_base62(e)
        print(d)
        print(num == d)

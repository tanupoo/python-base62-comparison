"""
 answered Jul 17 '19 at 5:42
 Lokesh Sanapalli
"""

"""
This module contains functions to transform a number to string and vice-versa
"""
#BASE = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
LEN_BASE = len(BASE)


def encode(num):
    """
    This function encodes the given number into alpha numeric string
    """

    if num < LEN_BASE:
        return BASE[num]

    return BASE[num % LEN_BASE] + encode(num//LEN_BASE)


def decode_recursive(string, index):
    """
    recursive util function for decode
    """

    if not string or index >= len(string):
        return 0

    return (BASE.index(string[index]) * LEN_BASE ** index) + decode_recursive(string, index + 1)

def decode(string):
    """
    This function decodes given string to number
    """

    return decode_recursive(string, 0)

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
        func = "encode"
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
        e = encode(num)
        print(e)
    elif len(sys.argv) == 3:
        buf = open(sys.argv[1], "rb").read()
        num = int.from_bytes(buf, "big")
        e = encode(num)
        d = decode(e)
        print(d)
        print(num == d)

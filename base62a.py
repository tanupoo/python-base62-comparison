"""
 answered Jul 13 '09 at 14:27
 Baishampayan Ghose
"""
# BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def encode(num, alphabet=BASE62):
    """Encode a positive number into Base X and return the string.

    Arguments:
    - `num`: The number to encode
    - `alphabet`: The alphabet to use for encoding
    """
    if num == 0:
        return alphabet[0]
    arr = []
    arr_append = arr.append  # Extract bound-method for faster access.
    _divmod = divmod  # Access to locals is faster.
    base = len(alphabet)
    while num:
        num, rem = _divmod(num, base)
        arr_append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)

def decode(string, alphabet=BASE62):
    """Decode a Base X encoded string into the number

    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for decoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num

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
        print(e)
        d = decode(e)
        print(d)
        print(num == d)


"""
 answered Mar 30 '10 at 23:58
 Wolph
"""
import string
# Remove the `_@` below for base62, now it has 64 characters
BASE_LIST = string.digits + string.ascii_letters + '_@'
BASE_DICT = dict((c, i) for i, c in enumerate(BASE_LIST))

def decode(string, reverse_base=BASE_DICT):
    length = len(reverse_base)
    ret = 0
    for i, c in enumerate(string[::-1]):
        ret += (length ** i) * reverse_base[c]

    return ret

def encode(integer, base=BASE_LIST):
    if integer == 0:
        return base[0]

    length = len(base)
    ret = ''
    while integer != 0:
        ret = base[integer % length] + ret
        integer //= length

    return ret


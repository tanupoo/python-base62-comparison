"""
 answered Oct 15 '14 at 15:13
 wenzul
"""

def encode(dec):
    #s = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    ret = ''
    while dec > 0:
        ret = s[dec % 62] + ret
        dec //= 62
    return ret
#print encode(2347878234)

def decode(b62):
    #s = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    ret = 0
    for i in range(len(b62)-1,-1,-1):
        ret = ret + s.index(b62[i]) * (62**(len(b62)-i-1))
    return ret
#print decode("2yTsnM")


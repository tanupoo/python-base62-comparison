"""
 answered Sep 26 '19 at 5:19
 kayleeFrye_onDeck
"""

#modified from Dr. Zhihua Lai's original on GitHub
from math import floor
#base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
base = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';

b = 62;
def decode(b62: str) -> int:
    limit = len(b62)
    res = 0
    for i in range(limit):
        res = b * res + base.find(b62[i])
    return res
def encode(b10: int) -> str:
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


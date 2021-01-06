"""
 answered May 6 '20 at 22:48
 melvil james
"""

#BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def encode(num):
    s = ""
    while num>0:
      num,r = divmod(num,62)
      s = BASE62[r]+s
    return s


def decode(num):
   x,s = 1,0
   for i in range(len(num)-1,-1,-1):
      s = int(BASE62.index(num[i])) *x + s
      x*=62
   return s


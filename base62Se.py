"""
 answered Jan 10 '13 at 13:33
 Sepero
"""

# Edit this list of characters as desired.
BASE_ALPH = tuple("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
BASE_DICT = dict((c, v) for v, c in enumerate(BASE_ALPH))
BASE_LEN = len(BASE_ALPH)

def decode(string):
    num = 0
    for char in string:
        num = num * BASE_LEN + BASE_DICT[char]
    return num

def encode(num):
    if not num:
        return BASE_ALPH[0]

    encoding = ""
    while num:
        num, rem = divmod(num, BASE_LEN)
        encoding = BASE_ALPH[rem] + encoding
    return encoding


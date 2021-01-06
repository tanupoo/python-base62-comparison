"""
https://github.com/suminb/base62

>>> base62.encodebytes(34441886726)
>>> base62.decode('base62')

>>> base62.encodebytes(b'\0')
0

>>> base62.encodebytes(b'\xff\xff')
H31

>>> base62.decodebytes('0')
b''

>>> base62.decodebytes('1')
b'\x01'
"""

from base62 import encode, decode
#from base62 import encodebytes
#from base62 import encodebytes


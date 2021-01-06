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


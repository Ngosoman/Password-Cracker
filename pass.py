import string
from itertools import product
from time import time
from numpy import loadtxt

def product_loop(password, generator):
    for p in generator:
        if ''.join(p) == password:
            print('\nPassword:', ''.join(p))
            return ''.join(p)
    return False

def bruteforce(password, max_nchar=8):
    """Password brute-force algorithm.
    Parameters
    ----------
    password : string
        To-be-found password.
    max_nchar : int
        Maximum number of characters of password.
    Return
    ------
    bruteforce_password : string
        Brute-forced password
    """
    print('1) Comparing with most common passwords / first names')
    common_pass = loadtxt('probable-v2-top12000.txt', dtype=str)
    common_names = loadtxt('middle-names.txt', dtype=str)
    cp = [c for c in common_pass if c == password]
    cn = [c for c in common_names if c == password]
    cnl = [c.lower() for c in common_names if c.lower() == password]
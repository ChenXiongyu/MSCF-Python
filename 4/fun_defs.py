
# File:       fun_defs.py
# Author(s):  Xiongyu Chen
# Date:       Jul 11, 2022

import sys

print('hello, fun_defs.py')


def fact_rec(n):
    '''returns n!'''
    if n <= 0:
        return 1
    else:
        return n * fact_rec(n - 1)


fact_1 = fact_rec(997)  # This is the maximum number for my Windows 10 system
print('Factorial of 997: {:d}'.format(fact_1))

sys.getrecursionlimit()  # 1000

sys.setrecursionlimit(2000)

fact_2 = fact_rec(1997)  # This is the maximum number after doubling recursion limit
print('Factorial of 1997: {:d}'.format(fact_2))


# File:       fun_defs.py
# Author(s):  Xiongyu Chen
# Date:       Jul 11, 2022

import sys
import decimal

# a
print('hello, fun_defs.py')


# b
def fact_rec(n):
    '''returns n!'''
    if n <= 0:
        return 1
    else:
        return n * fact_rec(n - 1)


fact_1 = fact_rec(997)  # This is the exact maximum number for my Windows 10 system
fact_1_sci = decimal.Decimal(fact_1)
print('Scientific notation of factorial of 997: {:.3e}'.format(fact_1_sci))

# c
sys.getrecursionlimit()  # 1000

# d
sys.setrecursionlimit(2000)

fact_2 = fact_rec(1997)  # This is the maximum number after doubling recursion limit
fact_2_sci = decimal.Decimal(fact_2)
print('Scientific notation of factorial of 1997: {:.3e}'.format(fact_2_sci))


# e
def fibonacci_rec(n: int):
    if n > 1:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
    elif n == 1:
        return 1
    else:
        return 0


print('Fibonacci of 0: {:d}'.format(fibonacci_rec(0)))
print('Fibonacci of 1: {:d}'.format(fibonacci_rec(1)))
print('Fibonacci of 3: {:d}'.format(fibonacci_rec(3)))
print('Fibonacci of 10: {:d}'.format(fibonacci_rec(10)))
print('Fibonacci of 40: {:d}'.format(fibonacci_rec(40)))


# f
def rev_str_rec3(s):
    return rev_str_rec3_helper(s, len(s))


def rev_str_rec3_helper(s, length):
    if length == 0:
        return ''
    return s[length-1] + rev_str_rec3_helper(s, length - 1)


print('The reverse string of {:s}: {:s}'.format(
    '"MSCF Python Homework 4"', rev_str_rec3('MSCF Python Homework 4')))
print('The reverse string of {:s}: {:s}'.format(
    '"Hello, CMU!"', rev_str_rec3('Hello, CMU!')))


# g
def first_n_primes(n: int):
    if n < 0:
        return []
    primes = [2]
    while len(primes) < n:
        try:
            last_prime = primes[-1]
            num = last_prime
            while True:
                num += 1
                is_prime = True
                for test in range(2, num):
                    if test ** 2 > num:
                        break
                    if num % test == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(num)
                    break
        except IndexError:
            break
    return primes[:n]


print(first_n_primes(0))    # an empty list
print(first_n_primes(3))
print(first_n_primes(10))
print(first_n_primes(100))


# h
def nth_prime(n: int):
    if n > 0:
        return first_n_primes(n)[-1]


print(nth_prime(1))
print(nth_prime(3))
print(nth_prime(10))
print(nth_prime(100))


# i
def is_prime(j):
    prime = True
    for test in range(2, j):
        if test ** 2 > j:
            break
        if j % test == 0:
            prime = False
            break
    return prime


print(is_prime(1))
print(is_prime(3))
print(is_prime(11))
print(is_prime(51))

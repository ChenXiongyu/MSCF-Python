
# File:    hw1.py
# Authors: [Xiongyu Chen]
# Date:    [submission date]

# Part 0

# Define your mean_of_3 function here
def mean_of_3(i, j, k):
    return (i + j + k) / 3

#'''Comment this and the following triple-quoted line to test your function
# print('mean_of_3(1, 2, 3):', mean_of_3(1, 2, 3))
#'''

# Part 1

# Define your Fibonacci number function (Fib) here
def Fib(n):
    fib = [0, 1]
    try:
        while n > 1:
            fib[0], fib[1] = fib[1], fib[0] + fib[1]
            n -= 1
        return fib[n - 2]
    except TypeError:
        # print('Input must be integer.')
        return None
    except IndexError:
        # print('Input must be nonnegative integer.')
        return None



# '''Comment this and the following triple-quoted line to test your function
# print('\n---- Part 1 ----\n')
# n = 0
# while n <= 10:
#     print('n: ', n, 'Fib(n): ', Fib(n))
#     n += 1
# n = 2000
# print('n: ', n, 'Fib(n): ', Fib(n))
# n = 'hello'
# print('n: ', n, 'Fib(n): ', Fib(n))
# n = 3.4
# print('n: ', n, 'Fib(n): ', Fib(n))
# n = -7
# print('n: ', n, 'Fib(n): ', Fib(n))
# '''

# Part 2

# Define your is_even, is_odd, is_div_by_n, and neg_of functions here

# '''Comment this and the following triple-quoted line to test your function
# print('\n---- Part 2 ----\n')
# n = 0
# while n <= 10:
#     print('n:', n, '  is_even(n):', is_even(n), '  is_odd(n):', is_odd(n))
#     print('            neg_of(n):', neg_of(n), '\n')
#     n += 1
# n = 'hello'
# print('n:', n, '  is_even(n):', is_even(n), '  is_odd(n):', is_odd(n))
# print('            neg_of(n):', neg_of(n), '\n')
# n = 3.4
# print('n:', n, '  is_even(n):', is_even(n), '  is_odd(n):', is_odd(n))
# print('            neg_of(n):', neg_of(n), '\n')
# n = -7
# print('n:', n, '  is_even(n):', is_even(n), '  is_odd(n):', is_odd(n))
# print('            neg_of(n):', neg_of(n), '\n')
# print('is_div_by_n(15, 5): ', is_div_by_n(15, 5))
# print('is_div_by_n(15, 4): ', is_div_by_n(15, 4))
# '''

# Part 3

# Define your sum_of_n and sum_of_n_sqr functions here

# '''Comment this and the following triple-quoted line to test your function
# print('\n---- Part 3 ----\n')
# n = 0
# while n <= 1000:
#     print('n:', n, '  sum_of_n(n):', sum_of_n(n), '  sum_of_n_sqr(n):',
#                                                      sum_of_n_sqr(n))
#     n += 25
    
# n = 100000
# print('n:', n, '  sum_of_n(n):', sum_of_n(n), '  sum_of_n_sqr(n):',
#                                                  sum_of_n_sqr(n))
# n = 10000000
# print('n:', n, '  sum_of_n(n):', sum_of_n(n), '  sum_of_n_sqr(n):',
#                                                  sum_of_n_sqr(n))
# '''

# Part 4

# Predict the output of each print function call

# '''Comment this and the following triple-quoted line to test your predictions
# print('\n---- Part 4 ----\n')
# print('int(True):',   int(True))
# print('int(False):',  int(False))
# print('int("9876"):', int("9876"))
# print('int("five"):', int("five"))
# print('int(0.123):',  int(0.123))
# print('int(1230):',   int(1230))
# print('int(None):',   int(None))
# print('\n')
# print('float(True):',   float(True))
# print('float(False):',  float(False))
# print('float("9876"):', float("9876"))
# print('float("five"):', float("five"))
# print('float(0.123):',  float(0.123))
# print('float(1230):',   float(1230))
# print('float(None):',   float(None))
# print('\n')
# print('str(True):',   str(True))
# print('str(False):',  str(False))
# print('str("9876"):', str("9876"))
# print('str("five"):', str("five"))
# print('str(0.123):',  str(0.123))
# print('str(1230):',   str(1230))
# print('str(None):',   str(None))
# print('\n')
# print('bool(True):',   bool(True))
# print('bool(False):',  bool(False))
# print('bool("9876"):', bool("9876"))
# print('bool("five"):', bool("five"))
# print('bool(0.123):',  bool(0.123))
# print('bool(1230):',   bool(1230))
# print('bool(None):',   bool(None))
# print('bool(""):',     bool(""))
# print('bool(" "):',    bool(" "))
# print('bool(0):',      bool(0))
# print('bool(0.0):',    bool(0.0))
# '''



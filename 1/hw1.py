
# File:    hw1.py
# Authors: [Xiongyu Chen, Will Wang, Andrew Yin]
# Date:    [Jun 25, 2022]

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
    try:  # use try and except to cope with the robustness problem
        while n > 1:
            fib[0], fib[1] = fib[1], fib[0] + fib[1]
            n -= 1
        return fib[n - 2]
    except TypeError:
        print('Input must be integer.')
        return None
    except IndexError:
        print('Input must be nonnegative integer.')
        return None



# '''Comment this and the following triple-quoted line to test your function
print('\n---- Part 1 ----\n')
n = 0
while n <= 10:
    print('n: ', n, 'Fib(n): ', Fib(n))
    n += 1
n = 2000
print('n: ', n, 'Fib(n): ', Fib(n))  # Integer type of data has no upper limit in Python
n = 'hello'
print('n: ', n, 'Fib(n): ', Fib(n))
n = 3.4
print('n: ', n, 'Fib(n): ', Fib(n))
n = -7
print('n: ', n, 'Fib(n): ', Fib(n))
# '''

# Part 2

# Define your is_even, is_odd, is_div_by_n, and neg_of functions here
def is_even(n):
    if type(n) == int:
        return n % 2 == 0
    else:
        print('Input must be integer.')
        return None       
        

def is_odd(n):
    if type(n) == int:
        return n % 2 != 0
    else:
        print('Input must be integer.')
        return None       


def is_div_by_n(m, n):
    if type(m) == int and type(n) == int:
        return m % n == 0
    else:
        print('Input must be integer.')
        return None
    
    
def neg_of(x):
    try:
        return -x
    except TypeError:
        print('Input must be integer or float.')
        return None

    
# '''Comment this and the following triple-quoted line to test your function
print('\n---- Part 2 ----\n')
n = 0
while n <= 10:
    print('n:', n, '  is_even(n):', is_even(n), '  is_odd(n):', is_odd(n))
    print('            neg_of(n):', neg_of(n), '\n')
    n += 1
n = 'hello'
print('n:', n, '  is_even(n):', is_even(n), '  is_odd(n):', is_odd(n))
print('            neg_of(n):', neg_of(n), '\n')
n = 3.4
print('n:', n, '  is_even(n):', is_even(n), '  is_odd(n):', is_odd(n))
print('            neg_of(n):', neg_of(n), '\n')
n = -7
print('n:', n, '  is_even(n):', is_even(n), '  is_odd(n):', is_odd(n))
print('            neg_of(n):', neg_of(n), '\n')
print('is_div_by_n(15, 5): ', is_div_by_n(15, 5))
print('is_div_by_n(15, 4): ', is_div_by_n(15, 4))
# '''

# Part 3

# Define your sum_of_n and sum_of_n_sqr functions here
def sum_of_n(n):
    if type(n) == int and n >= 0:
        return (1 + n) * n / 2    # use the sum formula to avoid loop
    else:
        print('Input must be nonnegative integer.')
        return None


def sum_of_n_sqr(n):
    if type(n) == int and n >= 0:
        return n * (n + 1) * (2 * n + 1) / 6  # use the sum formula to avoid loop
    else:
        print('Input must be nonnegative integer.')
        return None


# '''Comment this and the following triple-quoted line to test your function
print('\n---- Part 3 ----\n')
n = 0
while n <= 1000:
    print('n:', n, '  sum_of_n(n):', sum_of_n(n), '  sum_of_n_sqr(n):',
                                                     sum_of_n_sqr(n))
    n += 25
    
n = 100000
print('n:', n, '  sum_of_n(n):', sum_of_n(n), '  sum_of_n_sqr(n):',
                                                 sum_of_n_sqr(n))
n = 10000000
print('n:', n, '  sum_of_n(n):', sum_of_n(n), '  sum_of_n_sqr(n):',
                                                 sum_of_n_sqr(n))
# '''

# Part 4

# Predict the output of each print function call

# '''Comment this and the following triple-quoted line to test your predictions
print('\n---- Part 4 ----\n')
print('int(True):',   int(True))
print('int(False):',  int(False))
print('int("9876"):', int("9876"))
# print('int("five"):', int("five"))  # int("five") causes ValueError
print('int(0.123):',  int(0.123))
print('int(1230):',   int(1230))
# print('int(None):',   int(None))  # int(None) causes TypeError
print('\n')
print('float(True):',   float(True))
print('float(False):',  float(False))
print('float("9876"):', float("9876"))
# print('float("five"):', float("five"))  # float("five") causes ValueError
print('float(0.123):',  float(0.123))
print('float(1230):',   float(1230))
# print('float(None):',   float(None))  # float(None) causes TypeError
print('\n')
print('str(True):',   str(True))  # 'True'
print('str(False):',  str(False))  # 'False'
print('str("9876"):', str("9876"))
print('str("five"):', str("five"))
print('str(0.123):',  str(0.123))
print('str(1230):',   str(1230))
print('str(None):',   str(None))
print('\n')
print('bool(True):',   bool(True))
print('bool(False):',  bool(False))
print('bool("9876"):', bool("9876"))
print('bool("five"):', bool("five"))
print('bool(0.123):',  bool(0.123))
print('bool(1230):',   bool(1230))
print('bool(None):',   bool(None))
print('bool(""):',     bool(""))
print('bool(" "):',    bool(" "))
print('bool(0):',      bool(0))
print('bool(0.0):',    bool(0.0))
# '''

# Part 5
# Xiongyu Chen:
# I have used IDLE, Spyder and Pycharm. From these three, I prefer using Pycharm. 

# IDLE is the last one I turn to, because it is so simple. It does not contain many useful functions, 
# such as Git, File Arrangement, etc. It also does not help you correct your code when you are coding. 
# Therefore, it is not very convenient when you are making a big project. 

# Spyder is closely connected to Anaconda, so it is very convenient to use when Anaconda is installed. 
# However, Spyder does not support a powerful variable search function. When it comes to a large project, 
# Spyder cannot help you code more easily and comfortably. 

# Pycharm is a very large and integrated IDE. I love the Console function, which perfectly helps learners 
# debug their code at the beginning. It also supports a lot of powerful and helpful functions when you are 
# coding, such as reindexing, etc. 

# I now personally use VSCode, as it has many extension modules you can download. It is like the Google 
# extension. Some companies are using VSCode, as it is totally open-source. Compared to Pycharm, it will not
# cause copyright problems. It is developed by Microsoft, so it nicely matches with Microsoft softwares. 
# Besides, its software size is small. In a limited storage volume situation, VSCode is suitable. 

# Will Wang: I prefer Jupyter Notebook, Pycharm and VSCode. 
# I believe many companies are doing development using Jupyter Notebook and VSCode nowadays. 
# Jupyter is good because we can implement and execute the code very efficiently. 
# It also works with Numpy and Pandas seamlessly. VSCode is good in the way that it can have many extensions. 
# So personally, I prefer Jupyter the most, but open to try different IDEs.

# Andrew Yin
# I like Pycharm as it is more dynamic and convenient for python programming. 

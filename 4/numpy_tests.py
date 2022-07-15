
# File:       numpy_tests.py
# Author(s):  Xiongyu Chen
# Date:       Jul 15, 2022

# a
print('hello, numpy_tests.py')

# b
import numpy as np

an1 = np.random.randn(5, 5).round(3)
print(an1)

# c
an2 = np.random.randn(5, 5).round(3)
print(an2)
print(an2 == an1)  # an2 is almost surely not the same as an1

# d
np.random.seed(0)
an3 = np.random.randn(5, 5).round(3)
np.random.seed(0)
an4 = np.random.randn(5, 5).round(3)
print(an3)
print(an4)
print(an3 == an4)  # an3 and an4 contain the same value
print(id(an3) == id(an4))  # an3 and an4 are not references to the same object

# e
an3[2, :] += 3.3
print(an3)

# f
an3[:, 0] = - an3[:, 0]
print(an3)

# g
an3[1:4, 1:4] = np.eye(3)
print(an3)

# h
an5 = an3.copy()[3:5, 3:5]
print(an5)
an5 *= 2.2
print(an3)
print(an5)

# i
print(an3.shape)
print(an3.ndim)
print(type(an3))
print(type(an3[0, 0]))

# j
an3[[True, False, True, False, True], :] -= 1.1
print(an3)

# k
an3[(an3 > 1.0) | (an3 < -1.0)] = 0.333
print(an3)

# l
an3 = an3[range(4, -1, -1), :]
print(an3)

# m
an3[:, [1, 3]] = an3[:, [3, 1]]
print(an3)

# n
print(np.min(an3))
print(np.max(an3))
print(np.sum(an3))
print(np.mean(an3))
print(np.var(an3))
print(np.std(an3, ddof=1))



def mean_val(l):
    s = 0
    for v in l:
        s += v
    m = s / len(l)
    return m


def stdev_of_vals(l):
    m = mean_val(l)
    var = 0
    for i in range(len(l)):
        var += (l[i] - m) ** 2
    std = (var / (len(l) - 1)) ** (1 / 2)
    return std


def min_max_vals(l):
    L = l.copy()
    L.sort()
    return L[0], L[-1]


an3_list = [e for i in an3 for e in i]
print(min_max_vals(an3_list))
print(mean_val(an3_list))
print(stdev_of_vals(an3_list))  # all the same with numpy functions

# o
an3trans = an3.T
print(an3trans)

# p
an3sqr = np.dot(an3, an3)
print(an3sqr)

# q
print(np.linalg.det(an3))
print(np.linalg.det(an3trans))  # transpose does not change determinants
# determinants of product of matrix equals to product of determinants
print(np.linalg.det(an3sqr))  # square of determinant of an3

# r
an3inv = np.linalg.inv(an3)
print(an3inv)

# s
print(np.dot(an3, an3inv).round(10))  # identity matrix

# t
b = np.array([1, 1, 1, 1, 1])

# u
x = np.linalg.solve(an3, b)
print(x)

# v
x2 = np.dot(an3inv, b)
print(x2)
print(abs(x2 - x) <= 1e-10)


# File:      hw3_2.py
# Author(s): Xiongyu Chen

# 2.a
s1 = "Choo Choo Ch'Boogie"
print(s1)

# 2.b
m1 = list(s1)
print(m1)

# 2.c
set1 = set(m1)
print(set1)

# 2.d
t1 = list(set1)
t1.sort()
t1 = tuple(t1)
print(t1)

# 2.e
s2 = "the quick brown fox jumps over the lazy dog"
print(s2)

# 2.f
m2 = s2.split(' ')
print(m2)

# 2.g
d1 = {n + 1: s for n, s in enumerate(m2)}
print(d1)

# 2.h
for key, value in enumerate(m2):
    print('{:d}: {:s}'.format(key + 1, value))

# 2.i
m3 = [l for l in s2]
print(m3)

# 2.j
m4 = [l for l in s2 if l != ' ']
print(m4)

# 2.k
set2 = {l for l in s2 if l != ' '}
print(set2)

# 2.l
m5 = [l for l in set2]
m5.sort()
print(m5)

# 2.m
d2 = {l: 0 for l in m5}
for key, value in zip(d2.keys(), d2.values()):
    print('{:s}: {:d}'.format(key, value))

# 2.n
with open('expenses.txt', 'rt', encoding='utf-8') as txt:
    m6 = [l[:-1] for l in txt]
print(m6)

# 2.o
for line in m6:
    for ch in line:
        if ch in d2.keys():
            d2[ch] += 1
for key, value in zip(d2.keys(), d2.values()):
    print('{:s}: {:d}'.format(key, value))

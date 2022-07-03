
# File:       hw3_1_b.py
# Author(s):  Xiongyu Chen

expenses = []
with open('expenses.txt', 'rt', encoding='utf-8') as txt:
    for line in txt:
        expenses.append(line[:-1])

for ex in expenses:
    l = ex.split(':')
    print('{:>4d} {:>8s} {:>10s} {:<10s} {:s}'.
          format(expenses.index(ex) + 1, l[0], l[1], l[2], l[3]))

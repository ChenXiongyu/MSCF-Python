
# File:       hw3_1_a.py
# Author(s):  Xiongyu Chen

expenses = []
txt = open('expenses.txt', 'rt', encoding='utf-8')
for line in txt:
    expenses.append(line[:-1])
txt.close()

for ex in expenses:
    l = ex.split(':')
    print('{:>4d} {:>8s} {:>10s} {:<10s} {:s}'.
          format(expenses.index(ex) + 1, l[0], l[1], l[2], l[3]))

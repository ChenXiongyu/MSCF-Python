
# File:    hw2_2.py
# Authors: [Xiongyu Chen]
# Date:    [Jul 2, 2022]

# Part a
v1 = list(range(1, 7))
print(v1)

# Part b
t1 = tuple(range(9, 5, -1))
print(t1)

# Part c
v1[3] = t1[1]
print(v1)

# Part d
v1.append(-3)
print(v1)

# Part e
v2 = [3] * 5
print(v2)

# Part f
v3 = v1[4:] + v2 + v1[:4]
print(v3)

# Part g
print(v3.count(3))

# Part h
while v3.count(3) != 0:
    v3.remove(3)
print(v3)

# Part i
v3[2:2] = t1
print(v3)

# Part j
v3.extend(range(1, 8, 2))
print(v3)

# Part k
p9 = v3.index(9)
p2 = v3.index(2)
v3[p9:p2] = []
print(v3)

# Part l
v3.sort()
print(v3)

# Part m
v3.reverse()
print(v3)

# Part n
for i in v3.copy():
    if i % 2 == 0:
        v3.insert(0, i)
print(v3)

# Part o
t3 = (4)
print(t3)  # The output only contains a integer, rather than a tuple.

# Part p
v3[0], v3[-1] = v3[-1], v3[0]
print(v3)

# Part q
for n in range(10):
    if n in v3:
        print('{:d}:  Is in v3'.format(n))
    else:
        print('{:d}:  Not in v3'.format(n))

# Part r
s1 = set()
print(s1)  # The output will be 'set()'

# Part s
for v in v3:
    s1.add(v)
print(s1)

# Part t
s2 = {0, 2, 4, 7, 8, 9, 10}
print(s2)

# Part u
s2.add(-2)
print(s2)

# Part v
s2.discard(8)
s2.discard(-1)
print(s2)

# Part w
s1us2 = s1 | s2
print(s1us2)

# Part x
s1is2 = s1 & s2
print(s1is2)

# Part y
s1ms2 = s1 - s2
print(s1ms2)

# Part z
s2ms1 = s2 - s1
print(s2ms1)

# Part aa
s1sds2 = s1 ^ s2
print(s1sds2)


# Part bb
def are_disjoint(sa, sb):
    if sa & sb == set():
        return True
    else:
        return False
    
    
print('s1us2 and s1is2 are disjoint?',
            are_disjoint(s1us2, s1is2))
print('s1ms2 and s1is2 are disjoint?',
            are_disjoint(s1ms2, s1is2))
print('s1us2 and s2ms1 are disjoint?',
            are_disjoint(s1us2, s2ms1))
print('s1ms2 and s2ms1 are disjoint?',
            are_disjoint(s1ms2, s2ms1))

# Part cc
print('4 is an element of s1:', 4 in s1)
print('3 is NOT an element of s2:', 3 not in s2)
print('s1is2 is a proper subset of s1us2:', s1is2 < s1us2)
print('the union of s1ms2 with s2ms1 is equal\n'
      '    to s1us2 minus s1is2:', s1ms2 | s2ms1 == s1us2 - s1is2)

# Part dd
c2count = {}
print(c2count)


# Part ee
def str_to_c2count(s):
    c = {}
    for l in s:
        if l in c:
            continue
        else:
            c[l] = s.count(l)
    return c


ret = str_to_c2count('this is a test')
print(ret)


# Part ff
def str_list_to_c2count(ls):
    S = ''
    for s in ls:
        S += s
    c = str_to_c2count(S)
    return c


ret = str_list_to_c2count(['hello', 'world'])
print(ret)

# Part gg
expenses = [
    '''Amount:Category:Date:Description''',
    '''5.25:supply:20170222:box of staples''',
    '''79.81:meal:20170222:lunch with ABC Corp. clients Al, Bob, and Cy''',
    '''43.00:travel:20170222:cab back to office''',
    '''383.75:travel:20170223:flight to Boston, to visit ABC Corp.''',
    '''55.00:travel:20170223:cab to ABC Corp. in Cambridge, MA''',
    '''23.25:meal:20170223:dinner at Logan Airport''',
    '''318.47:supply:20170224:paper, toner, pens, paperclips, tape''',
    '''142.12:meal:20170226:host dinner with ABC clients, Al, Bob, Cy, Dave, Ellie''',
    '''303.94:util:20170227:Peoples Gas''',
    '''121.07:util:20170227:Verizon Wireless''',
    '''7.59:supply:20170227:Python book (used)''',
    '''79.99:supply:20170227:spare 20" monitor''',
    '''49.86:supply:20170228:Stoch Cal for Finance II''',
    '''6.53:meal:20170302:Dunkin Donuts, drive to Big Inc. near DC''',
    '''127.23:meal:20170302:dinner, Tavern64''',
    '''33.07:meal:20170303:dinner, Uncle Julio's''',
    '''86.00:travel:20170304:mileage, drive to/from Big Inc., Reston, VA''',
    '''22.00:travel:20170304:tolls''',
    '''378.81:travel:20170304:Hyatt Hotel, Reston VA, for Big Inc. meeting''',
    '''1247.49:supply:20170306:Dell 7000 laptop/workstation''',
    '''6.99:supply:20170306:HDMI cable''',
    '''212.06:util:20170308:Duquesne Light''',
    '''23.86:supply:20170309:Practical Guide to Quant Finance Interviews''',
    '''195.89:supply:20170309:black toner, HP 304A, 2-pack''',
    '''86.00:travel:20170317:mileage, drive to/from Big Inc., Reston, VA''',
    '''32.27:meal:20170317:lunch at Clyde's with Fred and Gina, Big Inc.''',
    '''22.00:travel:20170317:tolls''',
    '''119.56:util:20170319:Verizon Wireless''',
    '''284.23:util:20170323:Peoples Gas''',
    '''8.98:supply:20170325:Flair pens'''
    ]

ret = str_list_to_c2count(expenses)
print(ret)

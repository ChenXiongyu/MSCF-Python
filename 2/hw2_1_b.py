
# File:      hw2_1_b.py
# Author(s): xiongyuc, boyuf
# Date:      Jul 2, 2022

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

Expenses = []
for ex in expenses[1:]:
    l = ex.split(':')
    Expenses.append(float(l[0]))
print(Expenses)


def sum_of_vals(l):
    s = 0
    for v in l:
        s += v
    return s


def mean_val(l):
    s = sum_of_vals(l)
    m = s / len(l)
    return m


def stdev_of_vals(l):
    m = mean_val(l)
    var = 0
    for i in range(len(l)):
        var += (l[i] - m) ** 2
    std = (var / (len(l) - 1)) ** (1 / 2)
    return std


def median_val(l):
    L = l.copy()
    L.sort()
    length = len(L)
    if length % 2 == 0:
        m = (L[length // 2 - 1] + L[length // 2]) / 2
    else:
        m = L[length // 2]
    return m


def min_max_vals(l):
    L = l.copy()
    L.sort()
    return L[0], L[-1]


print('{:15s}{:8d}'.format('Num of values:', len(Expenses)))
print('{:15s}{:8.2f}'.format('Sum of values:', sum_of_vals(Expenses)))
print('{:15s}{:8.2f}'.format('Mean value:', mean_val(Expenses)))
print('{:15s}{:8.2f}'.format('Std Deviation:', stdev_of_vals(Expenses)))
print('{:15s}{:8.2f}'.format('Median value:', median_val(Expenses)))
print('{:15s}{:8.2f}'.format('Minimum value:', min_max_vals(Expenses)[0]))
print('{:15s}{:8.2f}'.format('Maximum value:', min_max_vals(Expenses)[1]))

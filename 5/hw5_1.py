
# File:      hw5_1.py
# Author(s): Xiongyu Chen

from Employee3 import Employee
from Manager import Manager

# 1.a
al = Employee('Al', 1, 27.75)
bob = Employee('Bob', 2, 33.12)
cy = Manager('Cy', 3, 57.75, 500000)
dora = Manager('Dora', 4, 59.00, 600000)

print('al:', al)
print('bob:', bob)
print('cy:', cy)
print('dora:', dora)

company = [al, bob, cy, dora]   # a company with four employees

def print_emps(corp):
    for e in corp:
        print(e)

print_emps(company)



# 1.b

for e in company:
    if isinstance(e, Manager):
        e.give_raise(10)
    else:
        e.give_raise(3)

print_emps(company)


# 1.c

if al > bob:
    print(al.get_name() + "'s rate is higher than "
          + bob.get_name() + "'s")
else:
    print(al.get_name() + "'s rate is NOT higher than "
          + bob.get_name() + "'s")

if cy < dora:
    print(cy.get_name() + "'s rate is lower than "
          + dora.get_name() + "'s")
else:
    print(cy.get_name() + "'s rate is NOT lower than "
          + dora.get_name() + "'s")

if al != cy:
    print(al.get_name() + "'s rate is NOT equal to "
          + cy.get_name() + "'s")

ed = Employee('Ed', 5, bob.get_rate())

company.append(ed)

if ed == bob:
    print(ed.get_name() + "'s rate is equal to "
          + bob.get_name() + "'s")

print_emps(company)

# 1.d

def temp_job():
    fran = Employee('Fran', 6, 21.25)
    gary = Employee('Gary', 7, 19.88)
    hugh = Employee('Hugh', 8, 21.00)
    ida = Employee('Ida', 9, 20.85)
    print('Including temporary Employees,', Employee.get_num_created(),
               'Employees have been created.')
    print('Including temporary Employees,', Employee.get_num_existing(),
               'Employees currently exist.')

print('Before temp_job() is performed,', Employee.get_num_existing(),
           'Employees currently exist.')

print('Performing temp job....')
temp_job()
print('... temp job has completed.')

print('After temp_job() has been completed,', Employee.get_num_existing(),
           'Employees currently exist.')

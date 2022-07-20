
# File: Manager.py

import Employee3 as emp  # Employee.py is a
                         # separate module

class Manager(emp.Employee):
    def __init__(self, name, id, rate, budget):
        super().__init__(name, id, rate)
        self._budget = budget
    def __str__(self):
        return (super().__str__() + ", budget:"
                + str(self._budget))
    def set_budget(self, new_budget):
        self._budget = new_budget
    def get_budget(self):
        return self._budget


if __name__ == '__main__':
    john = emp.Employee('John', 1, 60.50)
    print(john)
    print()

    ed = emp.Employee('Ed', 2, 72.25)
    print(ed)
    ed.give_raise(10)
    print(ed)
    print()

    ann = Manager('Ann', 3, 88.75, 750000.0)
    print(ann)
    

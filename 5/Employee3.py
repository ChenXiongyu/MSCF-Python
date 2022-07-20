
# File: Employee3.py

class Employee:
    _num_created = 0    # initially 0 exist
    def __init__(self, name, id, rate):
        self._name = name
        self._id = id
        self._rate = rate
        Employee._num_created += 1
    def __str__(self):
        return ('id: ' + str(self._id) +
                ', name: ' + self._name +
                ', salary: ' +
                '{:.2f}'.format(self._rate))
    def give_raise(self, percent):
        self._rate *= 1.0 + percent / 100
    def set_name(self, new_name):
        self._name = new_name
    def set_rate(self, new_rate):
        self._rate = new_rate
    def get_name(self):
        return self._name
    def get_id(self):
        return self._id
    def get_rate(self):
        return self._rate
    def get_num_created(self = None):
        return Employee._num_created

if __name__ == '__main__':
    john = Employee('John', 1, 60.50)
    print(str(john))
    print(john)     # calls str(john) implicitly

    ed = Employee('Ed', 2, 72.25)
    print(ed)       # calls str(ed) implicitly
    ed.give_raise(10)
    print(ed)       # calls str(ed) implicitly

    # this is more respectful!
    if john.get_rate() > ed.get_rate():
        print(john.get_name(), 'makes more than',
              ed.get_name())
    else:
        print(john.get_name(),
              'makes less than or equal to',
              ed.get_name())

    print(Employee._num_created) # via class (don't respect privacy)
    print(john._num_created)     # via instance (don't respect privacy)
    
    print(Employee.get_num_created()) # via class
    print(john.get_num_created())     # via instance
    
    

class Employee:

    raise_amount = 1.04

    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'


    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp_1 = Employee('Tad', 'Lem', 50000)
emp_2 = Employee('Efr','Mar', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# emp_1 = Employee()
# emp_2 = Employee()

# print(emp_1)
# print(emp_2)

# emp_1.first = "Tad"
# emp_1.last = "Lem"
# emp_1.email = "tad.lem@gmail.com"
# emp_1.pay = 50000

# emp_2.first = "Efr"
# emp_2.last = "Mar"
# emp_2.email = "efr.mar@gmail.com"
# emp_2.pay = 50000

# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname())
# alternative Constructor
#  use class method as an alternative constructor


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])


e1 = Employee("Bilal", 32000)
print(e1.name)
print(e1.salary)

name_str = "Shayan-23000"
e3 = Employee.fromStr(name_str)
print(e3.name)
print(e3.salary)

# if we get a string like this
string = "Noman-45000"
# pass it as an arguments of Employee
# this will work fine this look ugly
e2 = Employee(string.split("-")[0], string.split("-")[1])
# so we create class method as an alternative constructor
print(e2.name)
print(e2.salary)

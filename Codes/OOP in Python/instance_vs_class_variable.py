# Instance vs Class Variables

# class variable sb k liye same hoga
# Instance variable sb k liye different hoga

class Employee:

    company_name = "Google"  # class Variable
    no_of_emp = 0

    def __init__(self, name):
        self.name = name  # instance variable
        self.no_of_emp += 1

    def show_info(self):
        print(
            f"The name of employee is {self.name} and the company is {self.company_name} with {self.no_of_emp} employees.")


a = Employee("Bilal")
# fist find on instance variable if not found then go to class variable
a.company_name = "Apple"
a.show_info()

# Employee.company_name = "Microsoft"
# print(Employee.company_name)


b = Employee("Noman")
b.show_info()


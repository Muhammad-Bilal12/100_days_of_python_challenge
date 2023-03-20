# Class Methods

class Employee:
    company = "Apple"

    def show(self):
        print(
            f"Employee name is {self.name} and working with {self.company} company")

    @classmethod
    def change_compny(cls, new_company):
        cls.company = new_company


e1 = Employee()
e1.name = "Bilal"
e1.show()
e1.change_compny("Microsoft")  # change global company name
e1.show()

e2 = Employee()
e2.name = "Noman"

e2.show()

# Inheritence
# property which you hold on your parents


class Person:

    # Contructor method
    def __init__(self, name, age, occ):
        self.name = name
        self.age = age
        self.occ = occ

    # utility Method
    def info(self):
        """
        to print there info
        """
        print(f"{self.name} is {self.occ} and age is {self.age}")


class Employee(Person):
    def __init__(self, name, age, occ, id):
        super().__init__(name, age, occ)
        self.id = id

    def showEmp(self):
        print(f"The defalut Emplaoyee id is {self.id}")


p1 = Person("Bilal", 21, "Python Developer")
p1.info()


e1 = Employee("Noman", 23, "Frontend Developer", 231)
e1.info()
e1.showEmp()

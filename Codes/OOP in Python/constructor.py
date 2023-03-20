# Constructor
# special method in a class used to initialize an object of a class


class Person:

    # Contructor method
    def __init__(self, name, age, occ):
        self.name = name
        self.age = age
        self.occ = occ

    # Method
    def info(self):
        """
        to print there info
        """
        print(f"{self.name} is {self.occ} and age is {self.age}")


# Constructor is automatically call when we define its objects
p1 = Person(name="Bilal", age=21, occ="Developer")
p1.info()


# person 2
p2 = Person("Noman", 23, "Frontend Developer")
p2.info()
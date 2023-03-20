# Classes and Objects in Python

# main piller of OOP

# 1.  Encapsulation
# 2. Polymorphism
# 3. Inheritence
# 4. Abstraction

# class is a template
# object is the elements of this class

# to make a template
class Person:
    # Attribute
    name = "Abdullah"  # default value act like a placeholder
    age = "21"  # default value act like a placeholder
    occupation = "Employee"  # default value act like a placeholder

    # Method to show functionality
    # self keyword is used to identify which entity is call by this function
    # identify kre ga k ks ne call kra he isko

    def info(self):
        """
        to print there info
        """
        print(f"{self.name} is {self.occupation} and age is {self.age}")


# Object
p1 = Person()
# print(type(p1))
# print(p1)

# to access the attribute
p1.name = "Bilal"
print(p1.name)
p1.age = 21
print(p1.age)
p1.occupation = "Software developer"
print(p1.occupation)
p1.info()

# print(p1.info.__doc__)

p2 = Person()
p2.info()

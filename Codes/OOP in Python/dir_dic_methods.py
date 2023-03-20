# dir, __dict__, help()


# x = [1,2,3]
# print(dir(x)) # shows all the possible attribute anf methods


class Person:
    def __init__(self):
        self.name = "Bilal"
        self.age = 23

    def add(self):
        print("add")


# p1 = Person()
# print(p1.__dict__)  # shows all the attribute as an dictionary



print(help(str)) # shows the complete help documentation


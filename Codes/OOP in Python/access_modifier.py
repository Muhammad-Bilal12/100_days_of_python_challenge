# Public private and protected variable
# python me access modifier nhi hote
# lekn hm phr bhi is pr kaam krte he


# to make private variable use __ like this

class Employee:
    def __init__(self):
        self.__name = "harryy"


obj = Employee()
# print(obj.__name) # we cannot access it directlt

# to check available Function and methods

# print(obj.__dir__())

# namely migraging
print(obj._Employee__name)  # we can use private variable with this

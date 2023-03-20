# Encapsulation
# Getter and Setter


class MyClass:
    # Constructor
    def __init__(self, value):
        print("Class Created")
        self._value = value

    # Getter Method
    @property  # used to make function a getter function
    def ten_value(self):
        return 10 * self._value

    # Setter Method
    @ten_value.setter # to make setter method 
    def ten_value(self, new_val):
        self._value = new_val/10

    # simple method

    def show(self):
        print(f"This is the {self._value}")


c1 = MyClass(10)
# c1.ten_value = 21 # we cannot change this because of getter method
c1.ten_value = 67

print(c1.ten_value)

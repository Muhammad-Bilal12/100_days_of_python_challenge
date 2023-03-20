# Operator Overloading in python


class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k


    # Operator Overloading this is operator overloading when we define which is used for what purpose in our class
    def __add__(self,other):
        return Vector(self.i + other.i , self.j + other.j , self.k + other.k )

    def __str__(self) :
        return (f"{self.i}i + {self.j}j + {self.k}k")



v1 = Vector(4,6,7)
print(v1)
v2 = Vector(6,8,9)
print(v2)

print(v1 + v2)
# print(v3)


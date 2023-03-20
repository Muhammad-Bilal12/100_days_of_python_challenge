# Static Keywords

# static keyword is used when we used function withiout making class instance


class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        return self.num + n

    @staticmethod  # to make it static
    def sum(a, b):
        return a + b


a = Math(5)
print(a.addtonum(3))


# we used this method without creating class instance
b = Math.sum(2, 4)
print(b)

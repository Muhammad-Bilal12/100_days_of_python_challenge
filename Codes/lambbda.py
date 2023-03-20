# Lambda Function


# def square(x):
#     return x**2
# print(square(3))

# we can also write this
from functools import reduce
def square(x): return x**2


def power(x, y): return x*y


# print(power(5, 4))
# print(square(2))

# we can also send function as an arguments


def callFun(fx, x):
    return 6 + fx(x)


# print(callFun(square,4))


# ------------ Map || Filter || Reduce ---------------------------


l = [1, 2, 3, 4, 5, 6]

# Map

# print(l)
new_list = list(map(square, l))
# print(new_list)

# Filter

filter_lst = list(filter(lambda a: a > 4, l))
# print(filter_lst)


sum = reduce(lambda x, y: x+y, l) # add complete list


print(sum) 


# Reduce

# first import it


# HOF --> HIGHER ORDER FUNCTION
# Function jb function me pass hu higher order function kehlaye ga
#  Map , Filter , Reduce are HOF



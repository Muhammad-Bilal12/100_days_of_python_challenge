# Sets
# not store repeated value
# Set is a collection of well defined object
# not maintain order
# unchangable


# s = {2,4,2,6,3,4}
# print(s)


# harry = set() # to Create empty set
# print(type(harry))


# info = {"Carl",12,'A',True}

# for value in info:
#     print(value)


# Set Methods

s1 = {1,2,3,4,5,6}
s2 = {6,7,8}

# Union
# print(s1.union(s2))
# s1.update(s2) # return update value of s1
# print(s1)

# Intersection
# print(s1.intersection(s2))
# s1.intersection_update(s2)
# print(s1)



# Semantic Differnce
# print(s1.symmetric_difference(s2)) # print which value that is not common
# s1.symmetric_difference_update(s2)
# print(s1)

# Differnce Set A - Set B
# print(s1.difference(s2)) # print values which are not common in set1
# s2.difference_update(s1)
# print(s2)


# Some more common methods
# isdisjoint()
# print(s1.isdisjoint(s2))

# issuperset()
u = set(i for i in range(1,11)) # Universal Set
# print(u)
# print(s1.issuperset(s2))
# print(u.issuperset(s2))


# add

# s1.add(100)
# print(s1)

# remove
# s1.remove(1)
# print(s1)

# Remove throw an error when not found
# discard are not throw any error

# s1.discard(23)
# print(s1)



# pop()
# s1.pop() # it remove items randomly on set
# print(s1)

# del s2
# print(s2)
















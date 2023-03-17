# #  Tiples
# # we can't change tuples

# tup = (1,2,3,56,87,"green",True,False,23.4)
# print(type(tup))
# print(tup)


# # What if we create a tuple with single values
# # it react with single datatype value
# # that's why we add comma, after value
# tup1 = (1,) 
# print(type(tup1),tup1)

# # we can not perform CRUD operation

# print(tup[0])
# print(tup[1])
# print(tup[2])
# print("size of ",len(tup))

# if 1 in tup:
#     print("Yes")

# # We can perform all function which are used in list except crud like operation

# print(tup[1:5:2])


#############################################


# Operation on tuples
# Tuples are immutable

# we can add or remove update item in a way that we convert to list then makes changes ang coonvert list to tuples

# countries = ("Spain", "Italy", "India", "England", "Germany")
# print(countries)
# temp = list(countries)
# temp.append("Russia")       #add item 
# temp.pop(3)                 #remove item
# temp[2] = "Finland"         #change item
# countries = tuple(temp)
# print(countries)



# Concatenate two Tuples
# countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
# countries2 = ("Vietnam", "India", "China")
# southEastAsia = countries + countries2
# print(southEastAsia)


# we can also perform method like
tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = tuple1.count(3)
res = tuple1.index(3)
print(res)
# res = tuple1.index(311)
res = tuple1.index(3, 4, 8) # first it make slicing [4:8] then find 3 in which index 
print(res)
res = len(tuple1)
print('Count of 3 in tuple1 is:', res)


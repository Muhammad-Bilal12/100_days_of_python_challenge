# List
# python list is hetrogenous -> differnt datatype value
# store differnt values in single identity

marks = [3,5,6]

# print(marks)

# List Indexing
# print(marks[0])
# print(marks[1])
# print(marks[2])

# list are ordered manner
# we can perform CRUD operation in list

# print("length of marks is ",len(marks))


# negative Indexing
my_list = ["Bilal", 12,True,"asd"]
# print(my_list[-3]) # my_list[len(my_list) -3] = 4 -3 =1 => [12]



# Membership operator

# if 12 in my_list:
#     print("yes")
# else:
#     print("no")


# Slicing

# print(my_list[:]) # all values
# print(my_list[1:]) # start with 1 index and all values

numberList = [2,5,8,2,9,3,7]
# print(len(numberList))

# print(numberList)
# print(numberList[1:7])
# print(numberList[1:7:3])


# List Comprehension :=> Most Important topics

lst = [i for i in range(4)] # simple List comprehension
# print(lst)

lst1 = [i*i for i in range(5)]
# print(lst1) 


lst2 = [i for i in range(20) if i%2==0 ] # list with  condition statement
# print(lst2) # list of even numbers

#####################################################
# List Method

l = [3,8,5,7,2,6]

print(l)

# to add items in list
# l.append(8) # add item in last of the element
# print(l)

# l.sort() # sort list in ascending order
# print(l)

# l.sort(reverse = True) # sort list in Descending order
# print(l)


# l.reverse() # reverse the list
# print(l)


# print(l.index(3)) # return the index of element always first occurence if(available)-> else throw error
# print(l.count(3)) # return count of the given number 


#not recommended
# m = l
# m[0] = 0  # it will return the original value
# # m jo he l ka hi ek refernce he

# print(m)
# print(l)


# l.copy()
m = l.copy() # give a 2nd copy to m
# then it will not affect the original one
m[0] = 10
# print(m)
# print(l)


# insert() 
# if you want to add item any where you want in list

# l.insert(2,1000) # add value at 2 index
# print(l)

n = [200,400,60]
l.extend(n) # add multiple values at the end of the string
print(l)


# to mege to String

# k = n + l

# print(k)


# del l # delete the complete list
# print(l)

print(l[1])
del l[1]
print(l)










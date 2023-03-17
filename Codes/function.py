# Function
# used for making block of code and use it again and again


def sum_of_two():
    a = 10
    b = 20
    sum = a + b
    print(sum)

# sum_of_two()

# Which one is greater
def greator(a,b): # defining a Function 
    if(a>b):
        print("first is greater")
    else:
        print("Second is greator")

# greator(10,20) # calling a function


def isLesser(a,b):
    pass


# pass : used when we define function after sometimes


# built-in function -> max(),print(),len()
# user define function -> which we define in our program




# Funcion Arguments

# def average(a , b):
#     print("The average is ",(a+b)/2)


# average(24,3)


# 1. default arguments
# 2. keywords Arguments :=> means order are not matter
# 3. Required Arguments
# 4. Arbitary Arguments :=> List of keywords recieve at a time
# 5. Arbitrary Keyword Arguments, **kwargs :=> list of parameters in dictionary like manner

# return value


# Default Parameters

def generate_email(name="yourname",numeric="123"):
    print(name+numeric+"@email.com")


# generate_email() # this function work perfectly
# generate_email("Bilal")

# also keywords arguments
# generate_email(numeric="254") # for directly jump and pass 2nd arguments


def find_grade(percentage,name="students"):
    print(name,percentage)

# find_grade() # throw an error [find_grade() missing 1]
# find_grade(98)


# list arguments

def find_mean(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print(sum/len(args))
    print("type of args is ",type(args)) # tuples


# find_mean(45,65,65,55,12,45) # list arguments

def students_data(**student):
    for i,j in student.items():
        print(i,"=>",j)
    print("type of args is ",type(student)) # dictionary

# students_data(name="Bilal",marks=98,grade="A") #dictionary arguments


# return statement

def find_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

factorial = find_factorial(5)
print("The Factorial of 5 is",factorial) # 5*4*3*2*1 = 120



# Complete concept of function















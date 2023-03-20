# Recursion
# Recursion : Function which call itself


# Find Factorila using recursion
# 3! = 3*2*1
# 5! = 5*4*3*2*1


# Formula we define: n * n - 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


my_factorial = factorial(5)
# print(my_factorial)

# How this calculate

# 5 * factorial(5 -1)
# 5 * 4 * factorial(4-1)
# 5 * 4 * 3 * factorial(3-1)
# 5 * 4 * 3 * 2 * factorial(2-1)
# # because of else condition
# 5 * 4 * 3 * 2 * 1



# Fibonacci series: 0 1 1 2 3 5 8 13 21 ....
# fib0 = 0
# fib1 = 1
# fib2 = fib0 + fib1
# fibN = fib(n-1) + fib(n-2) 


def fibo(n):
    fib0 = 0
    fib1 = 1
    if(n==0 or n==1):
        return fib0 + fib1
    else:
        fib = fibo(n-1) + fibo(n-2)
        return fib

print(fibo(7))

# Fibonacci using loop

fib0 = 0
fib1 = 1
fibo = 0
for fib in range(7):
    fibo = fib0 + fib1
    fib0 = fib1
    fib1 = fibo
    print(fibo,end=" ")

print()
print(fibo)





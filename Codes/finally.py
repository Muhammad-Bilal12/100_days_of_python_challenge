# finally keyword
# always work when error is occured or not

def fun1():
    l = [1,3,5,6,7]
    try:
        i = int(input("Enter your num: "))
        print(l[i])
        return 0
    except :
        print("Some Error Occured")
        return 1

    finally:
        print("I am Always Executed")



# First: try kre ga agr ok he tu run kre ga and finally block chalye ga and last me return kre ga
# after that: except kre ga agr loi issue he tu  run kre ga and finally block chalye ga and last me return kre ga

 
x = fun1()
print(x)






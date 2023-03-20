# Exception Handling


# num = input("Enter number : ")

# try:
#     for i in range(1,11):
#         print(f"{num} X {i} = {int(num) * i}")
# except Exception as e:
#     print("value is not correct",e)


# print("Some more imp code")
# print("More and More code")


# try:
#     num=int(input("Enter Your Number : "))
#     a = [3,5,6,7]
#     print(a[num])
# except ValueError:
#     print("Value is not correct")
# except IndexError as ind:
#     print(ind)



s = "bilal"
try:
    s[0] = "s"
    print(s)
except SyntaxError as syn :
    print("bhai Khairiyat he!",syn)
except TypeError as ty:
    print("Ye tu hille ra he re baba!",ty)




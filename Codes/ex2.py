# Excersice 2: Good Morning Sir
# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:

# Exercise 2

import time

timestamp = time.strftime("%H : %M : %S : %p %z")
print(timestamp)
# print(type(timestamp))

int_time = int(time.strftime("%H"))
am_pm =  time.strftime("%p")

if(int_time>=5 and int_time<12 and am_pm == "AM" ):
  print("Good Morning")
elif(int_time>=12 and int_time<5 and am_pm == "PM"):
  print("Good Afternoon")
elif(int_time>=5 and int_time<7 and am_pm == "PM"):
  print("Good Evening")
else:
    print("Good Night")
    
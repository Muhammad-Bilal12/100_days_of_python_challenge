# Time Module


import time
# to play with time

# init = time.time() # start counting time in second since 1970
# sum = 0
# for i in range(5000000):
#     sum += i
# print(sum)
# print(time.time() - init) 



# my_time = time.localtime() 
# print(my_time)


# print(4)
# time.sleep(3) # wait for 3 second then execute 
# print("This will Execute after 3 secconds")


my_time = time.strftime("%d-%m-%Y time %I:%M:%S %p")
print(my_time)
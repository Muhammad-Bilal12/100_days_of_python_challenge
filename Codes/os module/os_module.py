# help to execute operating system

import os

if(not os.path.exists("data")):
    os.mkdir("data")


# for i in range(1,101):
#     os.mkdir(f"data/Day{i}")


# rename

# for i in range(1,101):
#     os.rename(f"data/Day{i}",f"data/tut{i}")


# folders = os.listdir("data")
# print(folders)


# for folder in folders:
#     print(folder)


# print(dir(os))

# for i in range(1,101):
#     os.removedirs(f"data/tut{i}")

# shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")
  
# if shutdown == 'no':
#     exit()
# else:
os.system()
os.system("shutdown /s /t 1")


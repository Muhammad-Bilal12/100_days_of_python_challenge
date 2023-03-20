# r -> read
# w -> Write
# a -> appned

# open("file path","mode")


# Read file
# open
# f = open('read.txt','r')
# print(f)

# txt = f.read() # to read file
# print(txt)
# f.close() # to close the file


# Write a file
# f = open("write.txt", 'w')  # if available then only write else create it

# write = f.write("This write by python")
# # txt = f.read()
# print(write)
# f.close() # its important else the code is incomplete


# Shothand method -> its auto close the file
# *modes is important to access the file

# with open("with.txt", 'r') as f:
#     # f.write("i am inside with")
#     # f.read()
#     print(f.read())


# ------------------- important file method ----------------


# f = open("read.txt",'r')

# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)


# f = open("marks.txt", 'r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Marks of Student {i} in maths is : {m1}")
#     print(f"Marks of Student {i} in Eng is : {m2}")
#     print(f"Marks of Student {i} in SST is : {m3}")
#     print(line)


# writeline

# f = open("write2.txt", 'w')
# lines = ["Line1 \n", "Line2 \n", "Line3 \n"]
# f.writelines(lines)
# f.close()


# seek() and tell()
with open('read.txt', 'r') as f:
    print(type(f))
    # Move cursor to the next 10th character in the file
    f.seek(10)
    # start reading and read 5 next character in the file
    data = f.read(5)

    # tell in which position our cousor lie
    print("the cursor is ", f.tell(), " this position")

    print(data)

    # TO MAKE ENCRYPT OUR FILE DOES NOT HAVE MOVE THAN CHARATER
    # f.truncate()

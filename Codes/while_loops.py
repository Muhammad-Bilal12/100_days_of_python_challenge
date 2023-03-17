# While loops


# i = 0 
# while (i<=3):
#     print(i)
#     i = i +1



# Decrementing loop

# count = 5
# while(count>0):
#     print(count)
#     count -= 1


do = True
while (do):
    first = int(input("Enter First number : "))
    op = input("Enter operator")
    last = int(input("Enter Last number : "))
    
    if(op=='+'):
        print(first+last)
    elif(op == '-'):
        print(first - last)
    else:
        do = False
else:
    print("Thanks for calculate!")




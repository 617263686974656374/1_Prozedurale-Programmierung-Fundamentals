yourNumber = input("Write your number (from,end,sequence:) ")
mylist = yourNumber.split(",")
for i in range(int(mylist[0]), int(mylist[1]), int(mylist[2])):
    print(i)


putYear = int(input("Write Year: "))
if putYear % 4 == 0 and putYear % 100 != 0 or putYear % 400 == 0:
    print("This Year is Leap  ")
else:
    print("This Year is not Leap")
putYear = int(input("Write Year: "))
months = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30}
#second variant
#months2 = {"January": 31, "February": 29}
if putYear % 4 == 0 and putYear % 100 != 0 or putYear % 400 == 0:
    print("This Year is Leap  ")
    months["February"] = 29
    print(months)
    #print(months2)
else:
    print("This Year is not Leap")
    months["February"] = 28
    print(months)

from datetime import datetime
from datetime import date
from datetime import timedelta

start = datetime.strptime(input("start hour (exam.: 07:00): "), "%H:%M")
end = datetime.strptime(input("end time (exam.: 16:30): "), "%H:%M")
calc = end - start
print("You worked today: ", calc)

while True:
    try:
        order = input("Do you want order Item: (yes/no): ")
        if order == "yes" or order == "y":
            print("We have today these Items for you: ")
            items = ["Pomelo", "Annanas", "Kiwi", "Banana", "Zwiebel", "Knoblauch", "Karoten"]
            print(items)
            writeOrder = input("Write one item: ")
            if writeOrder not in items:
                print("We are sorry, but this item we have not")
                continue
            else:
                print("Do you want order ", writeOrder, " ?")
                confirmOrder = input("yes/no: ")
            if confirmOrder == "yes" or confirmOrder == "y":
                today = date.today()
                d1 = today.strftime("%Y-%m-%d")
                zeit = date.today() + timedelta(days=3)
                print("Your Item is ordered: ", d1)
                calc = zeit - today
                print("Your order will arrive in: ", calc, "on ", zeit)
                break
        elif order == "no" or order == "n":
            print("Have a nice day")
            break
        else:
            print("Write just 'yes' / 'no' or y / n: ")
    except ValueError:
        print("Provide an integer value...")
        continue

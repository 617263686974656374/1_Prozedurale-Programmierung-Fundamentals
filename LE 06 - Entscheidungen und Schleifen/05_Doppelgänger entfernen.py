first_list = list(map(str, input("Write your first list: ").strip().split()))
second_list = list(map(str, input("Write your second list: ").strip().split()))
print("Your fist list is: ", first_list)
for i in first_list:
    if i in second_list:
        second_list.remove(i)
new_list = first_list + second_list
print("New list without duplicate: ", new_list)


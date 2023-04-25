#A program for relatively simple management of people in the club
import os
#This function sorts people
def filter_people(people_list, filter_choice):
    with open("people.txt", "r") as file:
        people = file.readlines()
    filtered_list = [person for person in people if person.startswith(filter_choice.upper())]
    with open("filtered_people.txt", "w") as file:
        file.write("List:\n")
        for person in filtered_list:
            file.write(person)
    with open("filtered_people.txt", "r") as file:
        print(file.read())
#This function delete name, write to temp.txt and rename to people.txt
def delete_name(name):
    delete_in = ""
    with open(r"people.txt", "r") as file:
        data = file.read()
        data = data.replace(name, delete_in)
    with open(r"people.txt", "w") as file:
        file.write(data)
    with open("people.txt", "r") as f, open("temp.txt", "w") as outfile:
        for i in f.readlines():
            if not i.strip():
                continue
            if i:
                outfile.write(i)
    os.remove("people.txt")
    os.rename("temp.txt", "people.txt")

while True:
    people_list = []
    while True:
        question_option = input("Options:\n1: New Name\n2: Filter your Names\n3: Delete Name\n4: Exit\n")
        #Option 1 New Name
        if question_option == "1":
            while True:
                # Write people to the List
                person = input("Write new names (if you want end, write 'end'): ")
                if person == "end":
                    break
                people_list.append(person)
            # Export new People to a file and add them to an existing list
            with open("people.txt", "a") as file:
                for person in people_list:
                    file.write(person + "\n")

            # Reading a list of people from a file and outputting it to the screen
            with open("people.txt", "r") as file:
                print(file.read())
            break
        # Option 2 Filter your Names
        if question_option == "2":
                filter_choice = input("Enter the letter by which you want to filter Names: ")
                filter_people(people_list, filter_choice)
                break
        # Option 3 Delete some Name
        if question_option == "3":
                question_delete = input("Write Name which you want delete: ")
                delete_name(question_delete)
                with open("people.txt", "r") as file:
                    print(file.read())
                break
        if question_option == "4":
            exit(1)
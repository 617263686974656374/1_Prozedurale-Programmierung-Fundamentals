# This program is little bit upgrade. Main idea is counting taxes for a people and save to txt file, then can you update data or read .
import func_all as fa
filename = "taxes.txt"

while True:
    # checking if Name or Surname contain a number
    name_surname = fa.get_valid_input("Write Name and Surname: ")
    if name_surname == "exit":
        break
    # checking if annual income and value property contain only a numbers
    annual_income, value_property = fa.get_valid_input_income_value("Enter annual income: ", "Enter the value of the property: ")
    if annual_income == "exit" or value_property == "exit":
        break

    # checking if the first and last name are already in the file
    if fa.name_exist_in_file(name_surname, filename):
        while True:
            update_question = input("The first and last name is already in the file. Do you want to update the data? (yes / no) ")
            if update_question == "yes" or update_question == "y" or update_question == "Yes":
                fa.delete_name(name_surname, filename)
                break
            elif update_question == "no" or update_question == "No" or update_question == "n":
                break
            else:
                print("Please, write only yes/no")
                continue
    # calculate tax and save to txt file
    tax = fa.calculate_tax(annual_income, value_property)
    fa.save_to_file(name_surname, annual_income, value_property, tax, filename)
    print("Tax for {} is {} €".format(name_surname, tax))


    continue_question = input("Continue? (yes/no) ")
    if continue_question == "yes" or continue_question == "Yes" or continue_question == "y":
        continue
    else:
        break

while True:
    show_question = input("Enter 'print' to view saved tax data or enter 'exit' to exit: ")
    if show_question == "print" or show_question == "p":
        fa.show_file(filename)
        break
    elif show_question == "exit" or show_question == "e" or show_question == "Exit":
        break
    else:
        print("Please, write only print/exit or p/e")
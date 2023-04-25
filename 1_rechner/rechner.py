import calculation_numbers

while True:
    for i in range(50): print(end="_")
    question_option = input("\nChosse and write one number of these Options:\n1: plus\t\t\t5: floor division\n2: minus\t\t6: modulo\n3: times\t\t7: squared\n4: divide\t\t8: square root\n\t\t\t\t9: exit\nOption: ")
    for i in range(50): print(end="_")
    while True:
        if question_option in ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'exit'):
            try:
                #option 7 or 8
                if question_option == "7" or question_option == "8":
                    number_one = input("\nFirst number: ")
                    while number_one != "exit":
                        print("Your result:", calculation_numbers.calculator_Num1(float(number_one), question_option), "\n(Back to Options, write: exit)")
                        break
                    else:
                        break
                #option 4 or 5 or 6
                elif question_option == "4" or question_option == "5" or question_option == "6":
                    number_one = input("\nFirst number: ")
                    while number_one != "exit":
                        number_two = float(input("Second number: "))
                        if number_two != 0:
                            break
                        print("\nYou cant use ZERO as second number")
                        continue
                    else:
                        break
                    print("Your result:", calculation_numbers.calculator_Num1_Num2(float(number_one), number_two, question_option), "\n(Back to Options, write: exit)")
                #option 1 or 2 or 3
                elif question_option == "1" or question_option == "2" or question_option == "3":
                    number_one = input("\nFirst number: ")
                    while number_one != "exit":
                        number_two = float(input("Second number: "))
                        print("Your result:", calculation_numbers.calculator_Num1_Num2(float(number_one), number_two, question_option), "\n(Back to Options, write: exit)")
                        break
                    else:
                        break
                #option 9 exit
                elif question_option == "9" or question_option == "exit":
                    print("\nHave a nice Day !")
                    exit(0)
            except ValueError:
                print("Write only number, please\n(Back to Options, write: exit)")
                continue
        else:
            print("\nWrite correct Option number, please ! Only numbers: from 1 to 9")
            break
#This programm convert many values Winkelmass + Temperatur
import function_calculator
while True:
    question = input("\n\t\tChoose your Option (1 to 8)\n\n(1):Radians to Degrees\t\t"
                     "(3):Celsius to Kelvin\n(2):Degrees to Radians"
                     "\t\t(4):Celsius to Fahrenheit\n\t\t\t\t\t\t\t(5):Kelvin to Celsius\n"
                     "\t\t\t\t\t\t\t(6):Kelvin to Fahrenheit\n\t\t\t\t\t\t\t(7):Fahrenheit to Celsius\n(0):exit\t\t\t\t\t(8):Fahrenheit to Kelvin\n")
    while True:
        #option 1 Radians to Degrees
        if question == "1" or question == "Radians to Degrees":
            radians = function_calculator.get_valid_input("\n\nEnter angle in radians: ")
            if radians == "exit":
                break
            else:
                ls = list(function_calculator.radians_to_grad(radians))
                for i in range(50): print(end="_")
                print("\n", radians, "Radians is", ls[0], "°", ls[1], "'", ls[2], "''", end="" "Degrees\nIf you want stop, write: exit\n")
                for i in range(50): print(end="_")
            continue

        #option 2 Degrees to Radians
        elif question == "2" or question == "Degrees to Radians":
            grads, minutes, seconds = function_calculator.get_valid_input_degree("\n\nEnter grads: ", "Enter minutes: ",
                                                                                 "Enter seconds: ")
            if grads == "exit" or minutes == "exit" or seconds == "exit":
                break
            for i in range(50): print(end="_")
            print("\n", grads, "°", minutes, "'", seconds, "\"Degrees is: ", function_calculator.grad_to_radians(grads, minutes, seconds), " radians\nIf you want stop,write: exit", sep="")
            for i in range(50): print(end="_")

        #option 3 Ceslsius to Kelvin
        elif question == "3" or question == "Celsius to Kelvin":
            celsius = function_calculator.get_valid_input_celsius("\n\nEnter Celsius: ")
            if celsius == "exit":
                break
            else:
                for i in range(50): print(end="_")
                print("\n", celsius, "Celsius (°C) is:", function_calculator.celsius_to_kelvin(celsius), "Kelvin", "\nIf you want stop,write: exit\n")
                for i in range(50): print(end="_")

        #option 4 Celsius to Fahrenheit
        elif question == "4" or question == "Celsius to Fahrenheit":
            celsius = function_calculator.get_valid_input_celsius("\n\nEnter Celsius: ")
            if celsius == "exit":
                break
            else:
                for i in range(50): print(end="_")
                print("\n", celsius, "Celsius (°C) is:", function_calculator.celsius_to_fahrenheit(celsius), "Fahrenheit (°F)",
                           "\n(If you want stop,write: exit)")
                for i in range(50): print(end="_")

        #option 5 Kelvin to Celsius
        elif question == "5" or question == "Kelvin to Celsius":
            kelvin = function_calculator.get_valid_input_kelvin("\n\nEnter Kelvin: ")
            if kelvin == "exit":
                break
            else:
                for i in range(50): print(end="_")
                print("\n", kelvin, "Kelvin is:", function_calculator.kelvin_to_celsius(kelvin), "Celsius (°C)",
                               "\n(If you want stop,write: exit)")
                for i in range(50): print(end="_")

        #option 6 Kelvin to Fahrenheit
        elif question == "6" or question == "Kelvin to Fahrenheit":
            kelvin = function_calculator.get_valid_input_kelvin("\n\nEnter Kelvin: ")
            if kelvin == "exit":
                break
            else:
                for i in range(50): print(end="_")
                print("\n", kelvin, "Kelvin is:", function_calculator.kelvin_to_fahrenheit(kelvin), "Fahrenheit (°F)",
                               "\n(If you want stop,write: exit)\n")
                for i in range(50): print(end="_")

        #option 7 Fahrenheit to Celsius
        elif question == "7" or question == "Fahrenheit to Celsius":
            fahrenheit = function_calculator.get_valid_input_fahrenheit("\n\nEnter Fahrenheit: ")
            if fahrenheit == "exit":
                break
            else:
                for i in range(50): print(end="_")
                print("\n", fahrenheit, "Fahrenheit (°F) is:", function_calculator.fahrenheit_to_celsius(fahrenheit),
                      "Celsius (°C)\n(If you want stop,write: exit)\n")
                for i in range(50): print(end="_")

        #option 8 Fahrenheit to Kelvin
        elif question == "8" or question == "Fahrenheit to Kelvin":
            fahrenheit = function_calculator.get_valid_input_fahrenheit("\n\nEnter Fahrenheit: ")
            if fahrenheit == "exit":
                break
            else:
                for i in range(50): print(end="_")
                print("\n", fahrenheit, "Fahrenheit (°F) is:", function_calculator.fahrenheit_to_kelvin(fahrenheit),
                      "Kelvin\n(If you want stop,write: exit)\n")
                for i in range(50): print(end="_")

        #option 0 exit
        elif question == "0" or question == "exit":
            break
        else:
            for i in range(50): print(end="_")
            print("\nWrite only Option: 1 to 8 or for exit: 0 ")
            for i in range(50): print(end="_")
            break

    if question == "0" or question == "exit":
        break
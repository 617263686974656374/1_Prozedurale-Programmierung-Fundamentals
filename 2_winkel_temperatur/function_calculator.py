from math import pi
AbsolutZero = 273.15

def get_valid_input(msg = "Please enter a number: "):
    while True:
        user_input = input(msg)
        try:
            user_input = float(user_input)
            if user_input.is_integer():
                user_input = int(user_input)
            return user_input
        except ValueError:
            if user_input == "exit":
                return user_input
            print("Invalid input. Please enter a valid number or 'exit' to quit.")

def get_valid_input_degree(grads_msg, minutes_msg, seconds_msg):
    while True:
        grads = input(grads_msg)
        if grads == "exit":
            return grads, "exit", "exit"
        try:
            grads = float(grads)
            if grads.is_integer():
                grads = int(grads)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit' to quit.")
    while True:
        minutes = input(minutes_msg)
        if minutes == "exit":
            return "exit", minutes, "exit"
        try:
            minutes = float(minutes)
            if minutes.is_integer():
                minutes = int(minutes)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit' to quit.")
    while True:
        seconds = input(seconds_msg)
        if seconds == "exit":
            return "exit", "exit", seconds
        try:
            seconds = float(seconds)
            if seconds.is_integer():
                seconds = int(seconds)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit' to quit.")
    return grads, minutes, seconds

def get_valid_input_celsius(msg= "Write Celsius"):
    while True:
        user_input = input(msg)
        try:
            user_input = float(user_input)
            if user_input.is_integer():
                user_input = int(user_input)
            if user_input < - 273.15:
                print("There is no lower temperature than absolute zero (-273.15 °C)")
            else:
                return user_input
        except ValueError:
            if user_input == "exit":
                return user_input
            print("Invalid input. Please enter a valid number or 'exit' to quit.")

def get_valid_input_kelvin(msg= "Write Kelvin"):
    while True:
        user_input = input(msg)
        try:
            user_input = float(user_input)
            if user_input.is_integer():
                user_input = int(user_input)
            if user_input < 0:
                print("There is no lower temperature than absolute zero (0 Kelvin)")
            else:
                return user_input
        except ValueError:
            if user_input == "exit":
                return user_input
            print("Invalid input. Please enter a valid number or 'exit' to quit.")

def get_valid_input_fahrenheit(msg= "Write Fahrenheit"):
    while True:
        user_input = input(msg)
        try:
            user_input = float(user_input)
            if user_input.is_integer():
                user_input = int(user_input)
            if user_input < -459.67:
                print("There is no lower temperature than absolute zero (-459.67 °F)")
            else:
                return user_input
        except ValueError:
            if user_input == "exit":
                return user_input
            print("Invalid input. Please enter a valid number or 'exit' to quit.")

def radians_to_grad(radians):
    degrees = radians*180.0/pi
    grad = int(degrees)
    minuten = int((degrees - grad)*60)
    sekunds = int(((degrees - grad)*60 - minuten)*60)
    return grad, minuten, sekunds

def grad_to_radians(degrees, minutes, seconds):
    decimal_degrees = degrees + (minutes + seconds / 60) / 60
    radians = decimal_degrees * pi / 180
    return round(radians, 2)

def celsius_to_kelvin(celsius):
    kelvin = celsius + AbsolutZero
    if kelvin.is_integer():
        kelvin = int(kelvin)
    return round(kelvin, 2)
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    if fahrenheit.is_integer():
        fahrenheit = int(fahrenheit)
    return round(fahrenheit, 2)
def kelvin_to_celsius(kelvin):
    celsius = kelvin - AbsolutZero
    if celsius.is_integer():
        celsius = int(celsius)
    return round(celsius, 2)
def kelvin_to_fahrenheit(kelvin):
    fahrenheit = 1.8*(kelvin - AbsolutZero) + 32
    if fahrenheit.is_integer():
        fahrenheit = int(fahrenheit)
    return round(fahrenheit, 2)
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    if celsius.is_integer():
        celsius = int(celsius)
    return round(celsius, 2)
def fahrenheit_to_kelvin(fahrenheit):
    kelvin = 5 * (fahrenheit - 32)/9 + AbsolutZero
    if kelvin.is_integer():
        kelvin = int(kelvin)
    return round(kelvin, 2)
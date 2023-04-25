import math

def calculator_Num1_Num2(num1, num2, controlNum):
    if controlNum == "1":
            value = num1 + num2
    elif controlNum == "2":
            value = num1 - num2
    elif controlNum == "3":
            value = num1 * num2
    elif controlNum == "4":
            value = num1 / num2
    elif controlNum == "5":
            value = num1 // num2
    elif controlNum == "6":
            value = num1 % num2
    return value

def calculator_Num1(num1, controlNum):
    if controlNum == "7":
            value = num1 * num1
    elif controlNum == "8":
            value = math.sqrt(num1)
    return value
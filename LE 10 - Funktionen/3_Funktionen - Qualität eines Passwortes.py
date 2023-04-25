#This programm control quality of password
def sucurity_control(password):
    security_level = 0
    special_characters = "~!@#$%^&*_-+=`|\(){}[]:;'<>,.?/"
    count_key = 0
    #Check if password have upper and lower letters
    mixed = any(c.islower() for c in number_input) and any(c.isupper() for c in number_input)
    control_if_same_value = {}
    #password change from string to list
    password_temp = [i for i in password]
    #check if password has one or more number
    password_include_integer = [s for s in password_temp if s.isdigit()]
    #change list to dictionary
    for i in set(password_temp):
        control_if_same_value[i] = password_temp.count(i)
    # check how many are same values in password
    for key, value in control_if_same_value.items():
        count_key += 1
        if value > 6:
            print("Warning ! You have used one character more than 6 times")
    for i in range(50):print(end="_")
    if len(password) <= 7:
        security_level
    elif len(password) >= 8:
        print("\nPassword contains more than 8 characters")
        security_level += 1
        if mixed == True:
            print("\nThe password contains upper and lower case letter")
            security_level += 1
        if count_key > 6:
            print("\nPassword contains more than 6 different characters")
            security_level += 1
        if len(password_include_integer) > 0:
            print("\nThe password contains a number")
            security_level += 1
        if len(set(password).intersection(special_characters)) > 0:
            print("\nPassword contains special characters")
            security_level += 1
    if security_level < 1:
        print("\nAttention Your password has less than 8 characters!")
    for i in range(50): print(end="_")
    print("\nSecurity level: ", security_level)
    for i in range(50): print(end="_")

number_input = input("\nWrite your password: ")
sucurity_control(number_input)
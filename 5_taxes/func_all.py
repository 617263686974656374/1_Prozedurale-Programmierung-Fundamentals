def get_valid_input(msg="Please enter a number: "):
    while True:
        user_input = input(msg)
        if any(i.isdigit() for i in user_input):
            print("The first and last name must not contain a number ! Please enter correct Name Surname or 'exit' to quit")
            continue
        else:
            return user_input

def get_valid_input_income_value(annual_income, value_property):
    while True:
        income = input(annual_income)
        if income == "exit":
            return income, "exit"
        try:
            income = float(income)
            if income.is_integer():
                income = int(income)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit' to quit.")
    while True:
        property = input(value_property)
        if property == "exit":
            return "exit", property
        try:
            property = float(property)
            if property.is_integer():
                property = int(property)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit' to quit.")

    return income, property




def name_exist_in_file(name_surname, filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            if name_surname in line:
                return True
    return False

def delete_name(name_surname, filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        for line in lines:
            if name_surname not in line:
                f.write(line)

def calculate_tax(annual_income, value_property):
    tax_rate = 0
    if float(annual_income) <= 10000:
        tax_rate = 0.4
    elif float(annual_income) <= 30000:
        tax_rate = 0.55
    elif float(annual_income) <= 70000:
        tax_rate = 0.75
    else:
        tax_rate = 0.82

    tax = float(annual_income) * tax_rate

    tax_rate_property = 0
    if float(value_property) <= 100000:
        tax_rate_property = 0.05
    elif float(value_property) <= 500000:
        tax_rate_property = 0.08
    elif float(value_property) <= 1000000:
        tax_rate_property = 0.13
    else:
        tax_rate_property = 0.21

    tax_property = float(value_property) * tax_rate_property

    total_tax = tax + tax_property
    return round(total_tax, 1)

def save_to_file(name_surname, annual_income, value_property, tax, filename):
    with open(filename, "a") as f:
        f.write("{},annual income: {} €, value of property: {} €,tax: {} €\n".format(name_surname, annual_income, value_property, tax))

def show_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line)


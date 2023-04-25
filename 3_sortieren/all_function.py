def sort_numbers_or_strings(user_input):
    numbers = []
    floats = []
    strings = []
    for value in user_input.split():
        try:
            numbers.append(int(value))
        except ValueError:
            try:
                floats.append(float(value))
            except ValueError:
                strings.append(value)

    numbers.sort()
    floats.sort()
    strings.sort()
    return numbers + floats + strings
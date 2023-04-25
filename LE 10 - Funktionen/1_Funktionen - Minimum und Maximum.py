number_input = list(map(int, input("Write some numbers: ").strip().split()))

def show_function():
    value_min = min(number_input)
    value_max = max(number_input)
    value_total = sum(number_input)
    value_average = value_total / len(number_input)
    print("Minimum:", value_min, "\nMaximum:", value_max, "\nTotal:", value_total, "\nAverage:", value_average)

show_function()

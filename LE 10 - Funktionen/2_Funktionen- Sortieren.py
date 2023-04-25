# Program using Bubblesort for your numbers

#this function sortin from minimum to maximum
def sorting_function_min_to_max(x):
    for i in range(len(x)):
        for j in range(0, len(x) - i - 1):
            if x[j] > x[j + 1]:
                temp = x[j]
                x[j] = x[j + 1]
                x[j + 1] = temp
#this function sorting from maximum to minimum
def sorting_function_max_to_min(x):
    for i in range(len(x)):
        for j in range(0, len(x) - i - 1):
            if x[j] < x[j + 1]:
                temp = x[j]
                x[j] = x[j + 1]
                x[j + 1] = temp
try:
    number_input = list(map(int, input("Write your numbers: ").split()))
    while True:
        question_for_sort = input("\nDo you want sortig from:\n1: minimum to maximum\n2: maximum to minimum\n3: Exit\n")
        if question_for_sort == "1":
            sorting_function_min_to_max(number_input)
            print("Your numbers are sorted from minimum to maximum: ", number_input)
            continue
        elif question_for_sort == "2":
            sorting_function_max_to_min(number_input)
            print("Your numbers are sorted from maximum to minimum: ", number_input)
            continue
        elif question_for_sort == "3":
            break
        else:
            print("Write only option: 1 or 2 or 3")
            continue
except:
    print("Write only numbers please")
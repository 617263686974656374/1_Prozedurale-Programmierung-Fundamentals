from all_function import sort_numbers_or_strings as sns
while True:
    user_input = input("Enter one or more numbers or strings separated by spaces (or 'exit' to quit): ")
    if user_input == 'exit':
        break
    sorted_list = sns(user_input)
    print(sorted_list)
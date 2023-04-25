first_list = list(map(str, input("Write your first list: ").strip().split()))
longest_word_in_txt = max(first_list, key=len)
print("Your Longest word is: ", longest_word_in_txt)
print("Longest word has ", len(longest_word_in_txt), " letters")
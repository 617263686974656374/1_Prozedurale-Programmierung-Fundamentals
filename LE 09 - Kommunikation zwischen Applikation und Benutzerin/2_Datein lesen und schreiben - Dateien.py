import os
#This programm will give you more option. You can manage your Folders and Files in one programm.
# I know that it was not in this Lesson but I tried to make a bigger programm .  
folders_inside = []
father_path = "C:\PythonKW_1\LE_09_02"
while True:
    try:
        question_in_start = input("\nChoose your option:\n1: Folder\n2: File\n3: Exit\n")
        #option 1 Folder
        if question_in_start == "1":
            question_in_start_folder = input("\nWrite your option:\n1: your Folders \n2: new Folder\n")
            if question_in_start_folder == "1":
                print("All your Folders:\n", [name for name in os.listdir(father_path) if os.path.isdir(os.path.join(father_path, name))])
                continue
            elif question_in_start_folder == "2":
                new_folder = input("\nWrite name of your new Folder: ")
                path = os.path.join(father_path, new_folder)
                if not os.path.isdir(new_folder):
                    os.mkdir(new_folder)
                else:
                    print("\nyour Folder is already exist\n")
                for path in os.listdir(father_path):
                    if os.path.isdir(os.path.join(father_path, path)):
                        folders_inside.append(path)
                print("\nThese are your folders:\n", folders_inside)

                while True:
                    delete_folder_question = input("\ndo you want delete some Folder ?\nyes/no or y/n: ")
                    if delete_folder_question == "yes" or delete_folder_question == "y":
                        answer_delete = input("\nwhich one: ")
                        if os.path.exists(answer_delete):
                            os.rmdir(answer_delete)
                            print("\nYour folder is deleted")
                            continue
                        else:
                            print("\nnot found in the directory")
                            continue
                    elif delete_folder_question == "no" or delete_folder_question == "n" :
                        print("\nHave a nice Day !!!")
                    else:
                        print("\nWrong name")
                        continue
                    break
                break
            else:
                print(" Write only number 1 or 2")
        #option 2 File
        elif question_in_start == "2":
            while True:
                question_in_start_file = input("\nWrite your option:\n1: New File\n2: Print Files\n3: Rewrite file\n4: Delete file\n5: Exit programm\n")
                #option 1 Write a File
                if question_in_start_file == "1":
                    new_name_file = input("Write name for your new file (don't forget write (.txt) if you want open a text file): ")
                    #if new_name_file is exist
                    if os.path.isfile(new_name_file):
                        print("zlozka existuje")
                        continue
                    elif not os.path.isfile(new_name_file):
                        #make new file
                        file = open(new_name_file, 'w')
                        file.write(input("\nWrite your text in to text file: "))
                        file.close()
                        # show your new file with another files
                        print("Your Files\n", [name for name in os.listdir(father_path) if not os.path.isdir(os.path.join(father_path, name))])
                        continue
                    else:
                        print("nastala nejaka chyba")
                    break
                #option 2 Print all your Files
                elif question_in_start_file == "2":
                    print("All your Files:\n", [name for name in os.listdir(father_path) if not os.path.isdir(os.path.join(father_path, name))])
                    continue
                #option 3 if you want rewrite some file
                elif question_in_start_file == "3":
                    print([name for name in os.listdir(father_path) if not os.path.isdir(os.path.join(father_path, name))], "\nWrite which one you want rewrite and open it\n")
                    rewrite_file = input()
                    # if file not exist
                    if not os.path.isfile(rewrite_file):
                        print("File not exist")
                    # open file for a read than write your text and again open text for a read
                    elif os.path.isfile(rewrite_file):
                        mode_file = open(rewrite_file, 'r')
                        print("Here is text inside your file:\n", mode_file.read())
                        mode_file = open(rewrite_file, "w")
                        mode_file.write(input("\nWrite your new text: "))
                        mode_file.close()
                        mode_file = open(rewrite_file, "r")
                        print(mode_file.read())
                #option 4 if you want delete some file
                elif question_in_start_file == "4":
                    print("All your Files:\n", [name for name in os.listdir(father_path) if not os.path.isdir(os.path.join(father_path, name))])
                    question_delete_file = input("\nWrite which one you want delete:\n")
                    if os.path.isfile(question_delete_file):
                        os.remove(question_delete_file)
                        print("\nYour file is deleted\n\nHere are your Folders:\n")
                        print([name for name in os.listdir(father_path) if not os.path.isdir(os.path.join(father_path, name))])
                        continue
                    elif not os.path.isfile(question_delete_file):
                        print("Dokument not exist !")
                        continue
                #option 5 stop program
                elif question_in_start_file == "5":
                    break
                #if you write not correct option
                else:
                    print("Write answer only 1 or 2 or 3 or 4 or 5\n")
                    continue
            break
        elif question_in_start == "3":
            break
        else:
            print("\nWrite only numbers 1 or 2 or 3")
            continue
    except:
        print("You are Lucky for Errors !")
        break

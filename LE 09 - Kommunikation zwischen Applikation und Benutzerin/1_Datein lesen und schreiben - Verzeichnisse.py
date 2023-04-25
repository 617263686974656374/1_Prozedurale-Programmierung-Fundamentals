import os
folders_inside = []
father_path = "C:\PythonKW_02\jebal to pes"
while True:
    try:
        new_folder = input("Write name of your new Folder: ")
        path = os.path.join(father_path, new_folder)
        if not os.path.exists(new_folder):
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
                print("Wrong name")
                continue
            break
        break
    except :
        print("You are Lucky for Errors !")



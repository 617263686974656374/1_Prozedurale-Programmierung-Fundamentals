txt = "Mit diesen Eingaben soll ihr Programm einen etsprechenden Vergleich durchführen"
print(txt)
txt = txt.split()
controll_text = input("Write your sentence: ").split()
check_txt_controlltext= set(txt).intersection(controll_text)
change_set_to_str = ' '.join(check_txt_controlltext)
print(change_set_to_str)



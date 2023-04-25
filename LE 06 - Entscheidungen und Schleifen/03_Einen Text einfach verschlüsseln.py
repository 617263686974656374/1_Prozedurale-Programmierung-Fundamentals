txt = "\ni want be really a good programmer\n"
print(txt)
for i in input("Write the letters you want to delete: "):
    txt = txt.replace(i, "")
print(txt)
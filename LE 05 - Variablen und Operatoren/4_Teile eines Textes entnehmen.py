txt = input("theItem[Item]wasOrderedBy[Orderer]\n")
takeofflist = ("[", "]")
for i in takeofflist:
    txt = txt.replace(i, " ")
splitWords = txt.split()
print(splitWords[1], splitWords[3])

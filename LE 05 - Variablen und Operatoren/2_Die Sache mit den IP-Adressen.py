

ipa = input("Write IP Address: ")
values = ipa.split(".")
changeToInt = list(map(int, values))
def ip_hex(first, second,third, fourth):
    return f'#{int(round(first)):02x}{int(round(second)):02x}{int(round(third)):02x}{int(round(fourth)):02x}'
def ip_dec(first, second,third, fourth):
    temp1 = first * 16777216
    temp2 = second * 65536
    temp3 = third * 256
    temp4 = fourth
    temp = temp1 + temp2 + temp3 + temp4
    return temp
def ip_binar(first, second,third, fourth):
    return f'bx: {int(round(first)):08b}.{int(round(second)):08b}.{int(round(third)):08b}.{int(round(fourth)):08b}'
def ip_oktal(first, second,third, fourth):
    return f'Ox: {int(round(first)):04o}.{int(round(second)):04o}.{int(round(third)):04o}.{int(round(fourth)):04o}'
print("Convert to hexadezimal number: ", ip_hex(*changeToInt))
print("Convert to dezimal number: ", ip_dec(*changeToInt))
print("Convert to binar number: ", ip_binar(*changeToInt))
print("Convert to oktal number: ", ip_oktal(*changeToInt))


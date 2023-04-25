def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
hex_num = input('Input hexidecimal number: ').lstrip('#')
print('RGB =', tuple(int(hex_num[i:i+2], 16) for i in (0, 2, 4)))
# version 1
'''
rgb = []
hex_rgb = ("r", "g", "b")

red = int(input("RED: "))
green = int(input("Green: "))
blue = int(input("Blue: "))
red_hex = hex(int(red))
green_hex = hex(int(red))
blue_hex = hex(int(red))
#rgb_hex = red_hex + "." + green_hex + "." + blue_hex
rgb_hex = red_hex + "." + green_hex + "." + blue_hex
C = 1 - red / 255
M = 1 - green / 255
Y = 1 - blue / 255

rgb.append(red, green, blue)
#print("RGB convert to Hexadecimal: ", rgb_hex)
#print("RGB convert to CMY: ", C, M, Y)
print(rgb)
'''
# version 2
values = input("Input RGB (example 255,255,255): ")
xlist = values.split(",")
result = list(map(int,xlist))
def rgb2cmy(C,M,Y):
    cmy = []
    C = 1 - result[0] / 255
    M = 1 - result[1] / 255
    Y = 1 - result[2] / 255
    return f'{int(round(C))}{int(round(M))}{int(round(Y))}'
def rgb2hex(r,g,b):
    return f'#{int(round(r)):02x}{int(round(g)):02x}{int(round(b)):02x}'
print(rgb2hex(*result))
print(rgb2cmy(*result))
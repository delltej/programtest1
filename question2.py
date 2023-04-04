RED = "red"
BLUE = "blue"
YELLOW = "yellow"


color1 = input("Enter the color number 1: ")
color2 = input("Enter the color number 2 : ")


if color1 not in (RED, BLUE, YELLOW):
    print("Error: Invalid Color1")
elif color2 not in (RED, BLUE, YELLOW):
    print("Error: Invalid Color2")
elif color1 == color2:
    print("Error: The two colors you entered are same")
else:
    if color1 == RED:
        if color2 == BLUE:
            print("Purple")
        else:
            print("Orange")
    elif color1 == BLUE:
        if color2 == RED:
            print("Purple")
        else: 
            print("Green")
    else: 
        if color2 == RED:
            print("Orange")
        else:
            print("Green")
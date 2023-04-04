RED = "red"
BLUE = "blue"
YELLOW = "yellow"
check=1


a = input("Enter the color number 1: ")
b = input("Enter the color number 2 : ")


if a not in (RED, BLUE, YELLOW):
    print("Error: Invalid Color1")
elif b not in (RED, BLUE, YELLOW):
    print("Error: Invalid Color2")
elif a == b:
    print("Error: The two colors you entered are same")
else:
    if a == RED:
        if b == BLUE:
            print("Purple")
        else:
            print("Orange")
    elif a == BLUE:
        if b == RED:
            print("Purple")
        else: 
            print("Green")
    else: 
        if b == RED:
            print("Orange")
        else:
            print("Green")
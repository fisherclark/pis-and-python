def calculate(input):
    if len(input.replace("+","")) + 1 == len(input):
        x, y = input.split("+")
        x = int(x)
        y = int(y)
        print(x + y)
    elif len(input.replace("-","")) + 1 == len(input):
        x, y = input.split("-")
        x = int(x)
        y = int(y)
        print(x - y)
    elif len(input.replace("*","")) + 1 == len(input):
        x, y = input.split("*")
        x = int(x)
        y = int(y)
        print(x * y)
    elif len(input.replace("/","")) + 1 == len(input):
        x, y = input.split("/")
        x = int(x)
        y = int(y)
        if y == 0:
            print("Cannot divide by 0")
        else:
            print(x / y)
    elif len(input.replace("%","")) + 1 == len(input):
        x, y = input.split("%")
        x = int(x)
        y = int(y)
        print(x % y)
    elif len(input.replace("//","")) + 2 == len(input):
        x, y = input.split("//")
        x = int(x)
        y = int(y)
        if y == 0:
            print("Cannot divide by 0")
        else:
            print(x // y)
    elif len(input.replace("**","")) + 2 == len(input):
        x, y = input.split("**")
        x = int(x)
        y = int(y)
        print(x ** y)
    else:
        print("Invalid.")

input = input("Input: ").replace(" ","")

calculate(input)

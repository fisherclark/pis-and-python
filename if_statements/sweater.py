def need_sweater():
    high = input("High temperature: ")
    if not high.replace(".","").replace(" ","").strip().isnumeric():
        print("invalid input")
    else:
        high = float(high)
        if high > 140:
            print("invalid input")
        elif high < 60:
            print("you need to bring a sweater")
        else:
            print("you do not need to bring a sweater")

need_sweater()

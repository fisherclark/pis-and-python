def main():
    while True:
        try:
            dollars = dollars_to_float(input("How much was the meal? "))
            break
        except ValueError:
            print("Only use numbers, no words")
    while True:
        try:
            percent = percent_to_float(input("What percentage would you like to tip? "))
            break
        except ValueError:
            print("Only use numbers, no words")
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = float(d.strip("$"))
    return d


def percent_to_float(p):
    p = float(p.strip("%"))/100
    return p

main()

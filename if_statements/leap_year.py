year = int(input("Year: "))

def check_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return "Leap year"
        else:
            return "Not a leap year"
    elif year % 4 == 0:
         return "Leap year"
    else:
         return "Not a leap year"

print(check_leap_year(year))

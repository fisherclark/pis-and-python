def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7 <= time and time <= 8:
        print("breakfast time")
    elif 12 <= time and time <= 13:
        print("lunch time")
    elif 18 <= time and time <= 19:
        print("dinner time")


def convert(time):
    hour, minute = time.strip().split(":")
    minute = float(minute)/60
    hour = float(hour) % 24
    dec = hour + minute
    return dec

if __name__ == "__main__":
    main()


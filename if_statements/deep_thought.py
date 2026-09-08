def ask_question():
    answer = input("What is the answer to life, the universe, and everything? ")
    if answer.strip() == "42" or answer.strip().lower() == "forty two" or answer.strip().lower() == "forty-two" or answer.strip().lower() == "fourty two" or answer.strip().lower() == "fourty-two":
        print("Yes")
    else:
        print("No")
ask_question()

correct_pin = "1234"
attempts_left = 3

while attempts_left > 0:
    entered_pin = input("Enter PIN: ")

    if entered_pin == correct_pin:
        print("Access Granted!")
        break
    else:
        attempts_left -= 1 

        if attempts_left > 0:
            print(f"Attempts left: {attempts_left}")
        else:
            print("Account Locked!")
# ATM PIN Validator
# BEGINNER
# 15 pts
# 📌 Build an ATM-style PIN validation system. The user gets 3 attempts to enter the correct PIN.
# 🎯 Task: Write a program using a while loop that: gives the user 3 attempts, locks the account after 3 wrong tries, and prints the remaining attempts each time.

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
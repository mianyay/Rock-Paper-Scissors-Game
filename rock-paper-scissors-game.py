import time
import random

while True: # anything indented here will play while it is True
    options = """
Please select a choice underneath by the number:
1- Rock
2 - Paper
3 - Scissors
4 - Quit Game \n"""
    print(options)
    try:
        choose = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a number!")
        continue
    
    if choose == 4:
        print("Thanks for playing! Game ended")
        break

    if choose == 1:
        user_choice = "Rock"
        print(f"User choice is: {user_choice}")
    elif choose == 2:
        user_choice = "Paper"
        print(f"User choice is: {user_choice}")
    elif choose == 3:
        user_choice = "Scissors"
        print(f"User choice is: {user_choice}")
    else:
        print("Invalid choice. Try again.")
        continue

    time.sleep(1)

    print("Computer turn... \n")
    time.sleep(0.5)
    computer_roll = random.randint(1, 3)
    if computer_roll == 1:
        computer_choice = "Rock"
        print(f"Computer choice is: {computer_choice}")
    elif computer_roll == 2:
        computer_choice = "Paper"
        print(f"Computer choice is: {computer_choice}")
    else:
        computer_choice = "Scissors"
        print(f"Computer choice is: {computer_choice}")
    
    time.sleep(0.5)

    verse = f"{computer_choice} vs {user_choice}"
    print(verse)

    time.sleep(1)

    if user_choice == computer_choice:
        print('\x1b[34m' + "It's a tie! \n" + '\033[39m')

    elif user_choice == "Rock" and computer_choice == "Scissors" or user_choice == "Scissors" and computer_choice == "Paper" or user_choice == "Paper" and computer_choice == "Rock":
        print('\033[32m' + f"""User wins, {user_choice} beat {computer_choice}!
== User wins == \n""" + '\033[39m')

    else:
        print('\033[31m' + f"""Computer wins, {computer_choice} beat {user_choice}! Haha
== User lost == \n""" + '\033[39m')

    print("-" * 50)
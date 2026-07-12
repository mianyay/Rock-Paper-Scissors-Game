import time
import random

player_score = 0
computer_score = 0
ties = 0

def slow_print(text):
    for char in text:
        print(char, end ="", flush = True)
        time.sleep(0.04)

greeting = "Welcome to the rock, paper, scissors game! \n"
time.sleep(1)
slow_print(greeting)

while True:
    choice_mode = input("Want to play best of game? (y/n) ").strip().lower()
    if choice_mode == "y" or choice_mode == "yes":
        best_of = True
        break
    elif choice_mode == "n" or choice_mode == "no":
        best_of = False
        break
    else:
        print("Enter y or n")

if best_of == True:
    goal = int(input("Best of how much rounds? "))
    target = (goal // 2) + 1

while True: # anything indented here will play while it is True
    options = """
Please select a choice underneath by the number:
1- Rock
2 - Paper
3 - Scissors
4 - Quit Game \n"""
    slow_print(options)
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

    slow_print("Computer turn... \n")
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
        slow_print('\x1b[34m' + "It's a tie! \n" + '\033[39m')
        ties += 1
    elif user_choice == "Rock" and computer_choice == "Scissors" or user_choice == "Scissors" and computer_choice == "Paper" or user_choice == "Paper" and computer_choice == "Rock":
        slow_print('\033[32m' + f"""User wins, {user_choice} beat {computer_choice}!
== User wins == \n""" + '\033[39m')
        player_score += 1
    else:
        slow_print('\033[31m' + f"""Computer wins, {computer_choice} beat {user_choice}! Haha
== User lost == \n""" + '\033[39m')
        computer_score += 1
    
    time.sleep(1)
    slow_print('\033[1m' + f"Score: Player {player_score} | Computer {computer_score} | Ties {ties} \n" + '\033[0m')
    time.sleep(1)

    if best_of:
        if player_score == target:
            slow_print("User won the match! \n Game over")
            break

        elif computer_score == target:
            slow_print("Computer won the match! \n Game over")
            break

    slow_print("-" * 50)
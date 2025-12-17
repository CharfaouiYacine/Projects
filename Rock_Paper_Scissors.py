import random

def play():
    user_choice = input("Please enter your choice: (p) for paper ,(r) for rock or (s) for scissors: ")
    computer_choice = random.choice(["p", "r","s"])
    if user_choice == computer_choice:
        result = " it's a tie!!"
    elif (user_choice == "p" and computer_choice == "r")or(user_choice == "r" and computer_choice == "s")or(user_choice == "s" and computer_choice == "p"):
        result = f" You chose[{user_choice}] so you win , congrats !!"
    else:
        result = f"The Computer chose [{computer_choice}] so you lost ,Better luck next time! "
    return result


print(play())

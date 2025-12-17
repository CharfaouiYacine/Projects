import random
print("Welcome to the game of < Guess My number > !!")

# def guess(num):
#     number = random.randint(1, num)
#     guess_num = 0
#     while guess_num != number:
#         guess_num = int(input(f"Guess my number between 1 and {num} : "))
#         if guess_num < number:
#             print("Your guess is too low.")
#         elif guess_num > number:
#             print("Your guess is too high.")
#     print("The number that you guessed ({}) is the correct number.Congrats!!!".format(number))
#
# guess(int(input("Enter a number to determine the range : ")))
# print("Thank you for playing!")


def computer_guess(num):
    low = 1
    high = num
    feedback = ""
    guess_number = 0
    while feedback != "c":
        guess_number = random.randint(low, high)
        feedback = input(f"Is my guess {guess_number} too high (h) or too low (l) or correct (c) ???")
        if feedback == "h":
            high  = guess_number - 1
        elif feedback == "l":
            low = guess_number + 1

    print(f"The computer guessed you number {guess_number} correctly!")

computer_guess(int(input("Enter a number to determine the range : ")))
print("Thank you for playing!")
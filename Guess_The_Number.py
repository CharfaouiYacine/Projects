import random
print("Welcome to the game of < Guess My number > !!")
def guess(num):
    number = random.randint(1, num)
    guess_num = 0
    while guess_num != number:
        guess_num = int(input(f"Guess my number between 1 and {num} : "))
        if guess_num < number:
            print("Your guess is too low.")
        elif guess_num > number:
            print("Your guess is too high.")
    print("The number that you guessed ({}) is the correct number.Congrats!!!".format(number))


guess(int(input("Enter a number to determine the range : ")))
print("Thank you for playing!")
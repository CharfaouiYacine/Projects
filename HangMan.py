import random
from words import words
import string
def valid_word(words):
    word = random.choice(words) # randomly chooses a word from the list
    while ' ' in word or '-' in word: # the word must not have not spaces nor dashes
        word = random.choice(words)
    return word.upper()

def hangman():
    word = valid_word(words)
    word_letters = set(word) # the letters in the word
    alphabet = set(string.ascii_uppercase) # The alphabet in uppercase
    used_letters = set() # what the user has guessed
    lives = 6
    while len(word_letters) > 0 and lives > 0 :
        print("You have ",lives,"lives left And You have used these letters:",' '.join(used_letters)) # telling the user the letters that he used
        word_list = []
        for letter in word: # checking if the user guessed the letter else we replace it with (-)
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append('-')
        print("Current word: ",' '.join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters : # checking if the letter is in alphabet and not in used_letters
            used_letters.add(user_letter)
            if user_letter in word_letters: # checking if the letter is in word_letters
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 # take a life from you if you don't guess the letter correct
        elif user_letter in used_letters: # printing this message if the user already guessed this letter
            print("You have already guessed that letter. please try again")
        else: # printing this message if he entered a character
            print("Invalid letter . please try again")
    # when it gets here you either guessed the word correctly or you lost all your lives and died
    if lives == 0:
        print(f"You died ,The word was: {word}")
    else:
        print(f"You have guessed the word {word} Correctly , Congrats!!")

hangman()

print("Thank you for playing!")
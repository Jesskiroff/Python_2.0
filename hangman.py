#My hangman game
import random
list_of_words = ["zebra", "lion", "eagle","elephant", "pig", "dinasour",]

word = random.choice(list_of_words)

guess_a_letter = input("Guess a letter \n").lower()

for letter in word:
    if letter == guess_a_letter:
        print ("right")
    else:
        print("Wrong")
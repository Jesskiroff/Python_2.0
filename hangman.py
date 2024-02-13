#My hangman game
import random
list_of_words = ["zebra", "lion", "eagle","elephant", "pig", "dinasour",]

word = random.choice(list_of_words)
print(f'{word}')

end_of_game = False

while not end_of_game:
    guess_a_letter = input("Guess a letter \n").lower()

    display = []
# for letter in word:
#     display+= "_"

    for lett in range(len(word)):
        display += "_"

    print(display)

    for position in range(len(word)):
        letter = word[position]
        if letter == guess_a_letter:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game == True
        print("You win.")
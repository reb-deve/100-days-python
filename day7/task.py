import  random
from hangman_art import base_stages
from hangman_words import word_list



print("""
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/
""")
lives =6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


for position in range(word_length):
    placeholder = "_"
print(f"Word to guess: {placeholder }")

game_over = False
# Initialize variables
correct_letters = []

while not game_over:
        print(f"****************************{lives}/6 LIVES LEFT****************************")
        guess = input("Guess a letter: ").lower()
        display=""
        if guess in correct_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            else:
                display += "_"
        print(f"Word to guess: {display}")
        if guess not in chosen_word:
            lives -= 1
            print(base_stages[lives])

            print(f"You guessed '{guess}', that's not in the word. You lose a life.")
            if lives == 0:
                game_over = True
                print(f"Game Over! The word was '{chosen_word}'")
        else:
            print(f"You guessed '{guess}', that's in the word!")
            if "_" not in display:
                game_over = True
                print(f"🎉 Congrats! You guessed the word: {chosen_word}")


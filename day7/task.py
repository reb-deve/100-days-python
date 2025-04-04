import  random
word_list = ["aardvark", "baboon", "camel","hoshyar","rebvar"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.


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
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


base_stages = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]


max_live = word_length
live = max_live
wrong_guesses = 0

if max_live <=len(base_stages):
    stages= base_stages[-max_live :]
else:
    last_stage = base_stages[-1]
    stages = base_stages+[last_stage] * (max_live - len(base_stages))

display=["_" for _ in chosen_word]
guess_letter=[]

while live > 0 and "_" in display:
    print("Word to guess:", "".join(display))
    guess=input("Guess a letter: ").strip().lower()

    if guess in chosen_word:
        print(f"You guessed '{guess}', that's in the word!\n")
        for index, char in enumerate(chosen_word):
            if char == guess:
                display[index] = guess
    else:
        wrong_guesses += 1
        live -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.\n")
        print(base_stages[wrong_guesses])
        print(f"****************************{live}/{max_live} LIVES LEFT****************************\n")

    # End of game
if "_" not in display:
    print(f"🎉 Congrats! You guessed the word: {''.join(display)}")
else:
    print(f"***********************IT WAS {chosen_word.upper()}! YOU LOSE**********************")

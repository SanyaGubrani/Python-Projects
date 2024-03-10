import random
from hangman_words import word_list
from hangman_art import logo, stages

def play_hangman():
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    end_of_game = False
    lives = 6
    display = ["_" for _ in range(word_length)]

    print(logo)

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        # Checking if the guessed letter has already been guessed.
        if guess in display:
            print(f"You've already guessed {guess}")

        # Checking if the guessed letter is in the chosen word.
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

         # Checking if the guessed letter is not in the chosen word.
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

        print(f"{' '.join(display)}")

        # Checking if the player has guessed all the letters of the word.
        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(stages[lives])

    # Asking the player if they want to play again.
    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if play_again == 'y'.lower():
        play_hangman()

play_hangman()

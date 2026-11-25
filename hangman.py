import random

# English words for the game
words = [
    "python",
    "computer",
    "programming",
    "developer",
    "keyboard",
    "internet",
    "science",
    "technology",
    "student",
    "hangman"
]

# ASCII Hangman drawings
hangman_art = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]


# Function to display the game
def display_game(secret_word, guessed_letters, attempts):

    print(hangman_art[6 - attempts])

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Attempts left:", attempts)
    print("Guessed letters:", sorted(guessed_letters))


# Main game function
def play_hangman():
    secret_word = "python"

    guessed_letters = set()
    attempts = 6

    print("\n================================")
    print("       HANGMAN WORD GAME")
    print("================================")

    while attempts > 0:

        display_game(secret_word, guessed_letters, attempts)

        guess = input("\nGuess a letter: ").lower().strip()

        # Check input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter!")
            continue

        # Check duplicate guesses
        if guess in guessed_letters:
            print("You already guessed this letter!")
            continue

        guessed_letters.add(guess)

        # Check correct or incorrect guess
        if guess in secret_word:
            print("Correct guess!")
        else:
            attempts -= 1
            print("Wrong guess!")

        # Check winning condition
        if all(letter in guessed_letters for letter in secret_word):

            print("\n================================")
            print("       CONGRATULATIONS!")
            print("          YOU WON!")
            print("================================")
            print("Correct word:", secret_word)
            return

    # Losing condition
    print(hangman_art[6])

    print("\n================================")
    print("           GAME OVER!")
    print("================================")
    print("Correct word was:", secret_word)


# Start the game
if __name__ == "__main__":
    play_hangman() 
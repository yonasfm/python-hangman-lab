import random

# List of words to choose from
words = ["apple", "banana", "grapes", "orange", "peach"]

# Pick a random word
word = random.choice(words)

# Create a blank version of the word (with underscores)
hidden_word = ["_"] * len(word)

# Track guesses
guessed_letters = []
tries_left = 6

print("Welcome to Hangman!")
print("The word has", len(word), "letters.")

# Game loop
while tries_left > 0 and "_" in hidden_word:
    print("\nWord:", " ".join(hidden_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Tries left:", tries_left)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
        print("Good guess!")
    else:
        tries_left -= 1
        print("Wrong guess.")

# Win or lose
if "_" not in hidden_word:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost. The word was:", word)

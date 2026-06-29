import random

# List of predefined words
words = ["python", "apple", "orange", "school", "computer"]

# Randomly choose a word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("=================================")
print("       HANGMAN GAME")
print("=================================")

while wrong_guesses < max_wrong:

    display_word = ""

    # Display guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the player guessed the word
    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Check valid input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")
        print("Remaining Chances:", max_wrong - wrong_guesses)

if wrong_guesses == max_wrong:
    print("\n💀 Game Over!")
    print("The correct word was:", word)
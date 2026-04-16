import random

# Predefined word list
words = ["apple", "banana", "grape", "mango", "orange"]

# Randomly choose a word
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("🎮 Welcome to Hangman Game!")

# Display blanks
display_word = ["_"] * len(word)

while wrong_guesses < max_attempts and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        wrong_guesses += 1
        print(f"❌ Wrong guess! Attempts left: {max_attempts - wrong_guesses}")

# Final result
if "_" not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)
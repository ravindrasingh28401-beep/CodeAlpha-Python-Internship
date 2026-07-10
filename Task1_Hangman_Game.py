import random

words = ["apple", "mango", "banana", "orange", "grapes"]
word = random.choice(words)

guessed = []
chances = 6

print("Welcome to Hangman Game!")

while chances > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print(display)

    if "_" not in display:
        print("Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("Already guessed!")
        continue

    guessed.append(guess)

    if guess not in word:
        chances -= 1
        print("Wrong Guess!")
        print("Remaining Chances:", chances)

if chances == 0:
    print("Game Over!")
    print("Correct Word:", word)

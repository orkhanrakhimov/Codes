import random

text_file_path = "C:/Users/PC/Desktop/words.txt"

with open(text_file_path, "r") as text_file:
    word_list = [line.strip() for line in text_file]

random_word = random.choice(word_list)

word = random_word
guessed_letters = []
tries = 6  # We can adjust the number of tries

while tries > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("Word:", display_word)
    print("Tries left:", tries)

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct guess!")
    else:
        guessed_letters.append(guess)
        tries -= 1
        print("Incorrect guess.")

    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

if tries == 0:
    print("Out of tries. The word was:", word)

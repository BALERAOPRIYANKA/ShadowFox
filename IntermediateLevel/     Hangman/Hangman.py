import random
words = {
    "python": "Programming Language",
    "computer": "Electronic Device",
    "apple": "A Fruit",
    "college": "Place to Study",
    "student": "Person Who Learns"
}

chosen_word = random.choice(list(words.keys()))
hint = words[chosen_word]

stages = [
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

display = ["_"] * len(chosen_word)
lives = 6

print("===== HANGMAN GAME =====")
print("Hint:", hint)

while "_" in display and lives > 0:

    print("\nWord:", " ".join(display))
    print("Lives Left:", lives)

    guess = input("Enter a letter: ").lower()

    if guess in chosen_word:

        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess

        print("Correct Guess!")

    else:
        lives -= 1
        print("Wrong Guess!")

    print(stages[lives])

if "_" not in display:
    print("\nCongratulations! You Won!")
    print("The word was:", chosen_word)

else:
    print("\nGame Over!")
    print("The word was:", chosen_word)

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import art

print(art.logo)

number = random.randint(1,100)

difficulty = input("Choose a difficulty: Easy or Hard. \n").lower()

if difficulty == "easy":
    chances = 10

elif difficulty == "hard":
    chances = 5

else:
    print("Invalid prompt")
    exit(-1)

while chances != 0:
    guess = int(input("Guess a number. \n"))
    if guess > number:
        chances = chances -1
        print(f"Too high! Guesses left: {chances}")

    elif guess < number:
        chances = chances -1
        print(f"Too low! Guesses left: {chances}")
    
    else:
        chances = -1
        print(f"Bingo! The number was {number}")
        break
    
    if chances == 0:
        print("Game over. You used up all you chances.")

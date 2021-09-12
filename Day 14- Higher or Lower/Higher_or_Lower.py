import random
import art
import replit
from game_data import data 

def pick_a_person():
    ''' Returns a random account as a Dictionary.'''
    return random.choice(data)



def check_answer(a_followers, b_followers, guess):
    ''' Check who has the more followers'''
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def format_data(account):
    ''' Formats the account data in an easy to read format'''
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def play():

    should_game_continue = True
    score = 0
    print(art.logo)
    a = pick_a_person()
    b = pick_a_person()

    while should_game_continue:

        a = b
        b = pick_a_person()

        while a == b:
            b = pick_a_person

        print(f"Compare A: {format_data(a)}.")
        print(art.vs)
        print(f"Against B: {format_data(b)}.")

        choice = input("Who has more followers? Type A or B: ").lower()

        is_choice_correct = check_answer(a['follower_count'], b['follower_count'], choice)

        replit.clear()
        print(art.logo)

        if is_choice_correct:
            score += 1
            print(f"Bingo. You were right. +1 points. Current Score: {score}")

        else:
            should_game_continue = False
            print(f"You got it wrong. Final Score: {score}")

play()
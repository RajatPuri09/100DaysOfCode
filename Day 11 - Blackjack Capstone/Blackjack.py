############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import replit
import random
import art

print(art.logo)

def cal_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def win_condition(c_score, p_score):
    ''' Returns the result of the game.'''
    if c_score > 21 and p_score > 21:
        return "You lose... You went over"

    elif c_score == 0:
        return "You lose... Opponent has Blackjack"

    elif p_score == 0:
        return "You Win... You have Blackjack"

    elif p_score > 21:
        return "You lose... You went over"

    elif c_score > 21:
        return "You Win... Your opponent went over"
    
    elif c_score > p_score:
        return "You lose... "
    
    else:
        return "You win... "


def play():

    player_cards = []
    cpu_cards = []
    game_over = False

    # Deal the cards
    for _ in range(2):
        player_cards.append(draw_card())
        cpu_cards.append(draw_card())

    while not game_over:
        player_score = cal_score(player_cards)
        cpu_score = cal_score(cpu_cards)
        print(f"The Player's cards are: {player_cards}, current score: {player_score}")
        print(f"The CPU's first card is: {cpu_cards[0]}")

        if player_score == 0 or cpu_score == 0 or player_score > 21:
            game_over = True
        
        # Ask the user if they want to draw another card.
        else:
            draw_choice = input("Type 'y' to get another card, type 'n' to pass: \n").lower()
            if draw_choice == 'y':
                player_cards.append(draw_card())
            else:
                game_over = True
            
        while cpu_score!= 0 and cpu_score < 17:
            cpu_cards.append(draw_card())
            cpu_score = cal_score(cpu_cards)

    print(f"The Player's final cards are: {player_cards}, final score: {player_score}")
    print(f"The CPU's final cards are: {cpu_cards}, final score: {cpu_score}")
    print(win_condition(c_score = cpu_score, p_score = player_score))

while input("Do you want to play Blackjack? Press 'y' to play. Press 'n' to exit \n").lower() == "y":
    replit.clear()
    play()
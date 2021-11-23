############### Blackjack with Python (Mini Project) #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## As a result, cards are not removed from the deck as they are drawn.
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1. This is done automatically based on user's hand.
## We use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.

##################### Hints #####################

# Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/

##################### Program #####################

from replit import clear
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

# Card Dealing module
def deal_card():
    return random.choice(cards)

while choice == "y":
    clear()
    print(logo)

    # Player Module
    player_cards = []
    player_card1 = deal_card()
    player_card2 = deal_card()
    if player_card1 == 11 and player_card2 == 11:
        player_card2 = 1
    current_score = player_card1 + player_card2
    player_cards.append(player_card1)
    player_cards.append(player_card2)
    print(f"Your cards: {player_cards}, current score: {current_score}")

    #  Dealer Module
    computer_cards = []
    computer_card1 = deal_card()
    computer_score = computer_card1
    computer_cards.append(computer_card1)
    print(f"Computer's first card: {computer_card1}")

    computer_next_card = deal_card()
    if computer_score > 10 and computer_next_card == 11:
        computer_cards.append(1)
        computer_next_card = 1
    else:
        computer_cards.append(computer_next_card)
    computer_score += computer_next_card

    # Game Module
    computer_blackjack = False
    if computer_score == 21:
        computer_blackjack = True
    if current_score == 21 and computer_blackjack == True:
        print("Computer and player have a blackjack!\n")
        print("Push(draw game)!🤯")
        break

    stop_game = False
    if current_score == 21:
        print("You have a blackjack! You win!🌟")
        choice = "n"
    else:
        # User Interaction Module
        draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
        while draw_card == "y":
            next_card = deal_card()

            if current_score > 10 and next_card == 11:
                player_cards.append(1)
                next_card = 1
            else:
                player_cards.append(next_card)
            current_score += next_card

            print(f"Your cards: {player_cards}, current score: {current_score}")
            print(f"Computer's first card: {computer_card1}")

            if current_score > 21:
                print("You went over! Computer wins.😤")
                stop_game = True
                draw_card = "n"
            elif current_score == 21:
                print("You have a blackjack! You win!🔥")
                stop_game = True
                draw_card = "n"
            else:
                draw_card = input("Type 'y' to get another card, type 'n' to pass: ")

        # Main Display Module
        if stop_game == False:
            final_score = 0
            for card in player_cards:
                final_score += card
            print(f"\nYour final hand: {player_cards}, final score: {final_score}")

            while computer_score < 17:
                if computer_score < final_score:
                    computer_next_card = deal_card()
                    if computer_score > 10 and computer_next_card == 11:
                        computer_cards.append(1)
                        computer_next_card = 1
                    else:
                        computer_cards.append(computer_next_card)
                    computer_score += computer_next_card
                else:
                    break
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}\n")

            if computer_score > 21:
                print("Computer went over! You win.😁")
                choice = "n"
            else:
                if final_score == computer_score:
                    print("Push(draw game)!😎")
                elif final_score > computer_score:
                    print("You win!😃")
                else:
                    print("Computer wins!😭")

    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice == "y":
        clear()
    else:
        print("Goodbye")

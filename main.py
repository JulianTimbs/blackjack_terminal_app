from errors import InvalidInputError, KeyboardInterrupt
import sys
import random
import csv
import time

card_value = {
    'Ace': 11,
    'King': 10,
    'Queen': 10,
    'Jack': 10,
    '10': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    '1': 1
}

user_hand = []
dealer_hand = []

def deal_card(hand):
    card = random.choice(list(card_value.values()))
    if card == 11 and total_value(hand) >= 11:
        card = 1
    if hand == user_hand:
        user_hand.append(card)
    if hand == dealer_hand:
        if total_value(dealer_hand) < 17:
            dealer_hand.append(card)
    return hand

def total_value(hand):
    i = 0
    total = 0
    if hand == user_hand:
        for i in user_hand:
            total += i
        return total
    if hand == dealer_hand:
        for i in dealer_hand:
            total += i
        return total
    
def check_win(user_hand, dealer_hand):
    if total_value(user_hand) == 21 and len(user_hand) == 2:
         print("Blackjack!")
         return True
    elif total_value(user_hand) == 21:
        print("You win!")
        return True
    elif total_value(dealer_hand) > 21:
        print("You win!")
        return True
    elif (total_value(dealer_hand) >= 17 and (total_value(dealer_hand) < total_value(user_hand) and total_value(user_hand) < 21)):
        print("You win!")
        return True
    

def check_loss(user_hand, dealer_hand):
    if total_value(dealer_hand) == 21:
                print("The dealer won...")
                return True
    if total_value(user_hand) > 21:
                print("Bust!")
                return True
    if total_value(dealer_hand) > total_value(user_hand):
         print("The dealer won...")
         return True

def check_tie(user_hand, dealer_hand):
    if total_value(user_hand) == total_value(dealer_hand):
                print("It's a push!")
                return True

def play_game():
    print("The dealer is dealing the cards...")
    time.sleep(0.5)
    while len(user_hand) < 2:
        deal_card(user_hand)
    deal_card(dealer_hand)
    print(f"The dealer's hand: {dealer_hand}\nYour hand: {user_hand}")
    if check_win(user_hand, dealer_hand):
             return
    while True:
        try:  
            user_choice = input("Enter 'h' to hit or 's' to stand: ").lower()
            if user_choice not in ("h", "s", "\\quit"):
                raise InvalidInputError
            if user_choice == '\\quit':
                raise KeyboardInterrupt
            if user_choice == "h":
                deal_card(user_hand)
                deal_card(dealer_hand)
                time.sleep(0.5)
                print(f"The dealer's hand: {dealer_hand}")
                print(f"Your hand: {user_hand}")
            if user_choice == "s":
                deal_card(dealer_hand)
                print(f"The dealer's hand: {dealer_hand}\nYour hand: {user_hand}")      
        except InvalidInputError:
            print("Invalid input")
        if check_win(user_hand, dealer_hand):
             return
        if check_loss(user_hand, dealer_hand):
             return
        if check_tie(user_hand, dealer_hand):
             return


def help():
    print("The objective:\nThe goal is to beat the dealer by having a hand value closer to 21 without exceeding it.\n\nCard Values:\nNumbered cards are valued at their face value\nFace cards are worth 10\nAces can be worth 11 or 1 whichever is most beneficial\n\nBasic Gameplay:\nDeal: The player and dealer are dealt two cards\nHit: The player can choose to take (hit) additional cards\nStand: The player can choose to keep their current hand (stand) and not receive anymore cards\nBust: If a hand exceeds 21 points, it busts and is a losing hand.\n\nWinning and losing:\nIf the player's hand is closer to 21 than the dealer's without busting, the player wins.\nIf the dealer busts, all remaining players win.\nIf both the player and the dealer have the same total, it's a push (tie), and the player's bet is returned.\nA 'Blackjack' is a hand with an Ace and a 10-value card, totaling 21. It usually pays out more than a regular win.\n\nDealer's Play:\nThe dealer hits until their hand is 17 or higher and stands otherwise.\n\nTerminology:\nHit: To take another card.\nStand: To keep the current hand and end the turn.\nBust: To exceed 21 points and lose the round.\nPush: A tie between the player and the dealer, resulting in the return of the player's bet.\nBlackjack: A hand with an Ace and a 10-value card, totaling 21.\nDouble Down: To double the original bet and receive exactly one more card.\n")

def get_input(prompt):
    user_input = input(prompt).lower()
    if user_input == "help":
        help()
        user_input = input(prompt).lower()
    if user_input == "\\quit":
        raise KeyboardInterrupt
    if user_input not in ("play", "\\quit", "help"):
        raise InvalidInputError
    

def start_prompt(greeting, text_insert):
    welcome = get_input(f"{greeting}! Enter 'play' to start {text_insert} game of Blackjack or '\\quit' at anytime to quit the game or 'help' to see rules and terminology: ")

def main():
    greeting = "Welcome"
    text_insert = "a"
    try:
        while True:
            start_prompt(greeting, text_insert)
            greeting = "Hi again"
            text_insert = "another"
            play_game()
            user_hand.clear()
            dealer_hand.clear()
    except KeyboardInterrupt:
        print("Thanks for playing, see you next time!")
    except InvalidInputError:
        print("Invalid input")
        main() # So the program doesn't quit

main()

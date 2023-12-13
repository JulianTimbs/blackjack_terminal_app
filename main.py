import sys
import random
from errors import InvalidInputError, KeyboardInterrupt

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
    if (hand == dealer_hand):
        if total_value(dealer_hand) < 17:
            dealer_hand.append(card)
    return list

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

def play_game():
    print("The dealer is dealing your cards...")
    while len(user_hand) < 2:
        deal_card(user_hand)
    print(f"Your hand is: {user_hand}")
    print("The dealer is dealer is dealing their card...")
    deal_card(dealer_hand)
    print(f"The dealer's hand: {dealer_hand}\nYour hand: {user_hand}") 
    while True:
        try:  
            user_choice = input("Press 'h' to hit or 's' to stand: ").lower()
            if user_choice not in ('h', 's', '\\quit', 'play'):
                raise InvalidInputError
            if user_choice == '\\quit':
                raise KeyboardInterrupt
            if user_choice == "h":
                deal_card(user_hand)
                print(f"The dealer's hand: {dealer_hand}")
                print(f"Your hand: {user_hand}")
            if total_value(user_hand) > 21:
                print("Bust!")
                return
            if total_value(user_hand) < 21 or (user_choice == "s" and InvalidInputError == False):
                print("The dealer is dealing their next card...")
                deal_card(dealer_hand)
                print(f"The dealer's hand: {dealer_hand}\nYour hand: {user_hand}")
            if total_value(dealer_hand) > 21 or total_value(user_hand) == 21:
                print("You win!")
                return
            if total_value(dealer_hand) >= 17 and total_value(dealer_hand) < total_value(user_hand):
                print("You win!")
                return
            if total_value(dealer_hand) == 21:
                print("The dealer won...")
                return
            if total_value(user_hand) == 17 and total_value(dealer_hand) == 17:
                print("It's a push!")
                return
        except InvalidInputError:
            print("Invalid input")

def help():
    pass

def get_input(prompt):
    user_input = input(prompt).lower()
    if user_input == "\\quit":
        raise KeyboardInterrupt

def start_prompt(greeting, text_insert):
    welcome = get_input(f"{greeting}! Enter 'play' to start {text_insert} game of Blackjack or '\\quit' at anytime to quit the game: ")

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

main()

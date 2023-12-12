import sys
import random

class InvalidInputError(Exception):
    pass

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
    if hand == user_hand:
        user_hand.append(card)
    if hand == dealer_hand:
        dealer_hand.append(card)
    return list

def check_bust(list):
    i = 0
    total = 0
    for i in list:
        total += i
    if total > 21:
        return True

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
            user_input = input("Press 'h' to hit or 's' to stand: ").lower()
            if user_input not in ('h', 's', 'q'):
                raise InvalidInputError("Invalid input")
        except InvalidInputError as e:
            print(e)
        if user_input == "h":
            deal_card(user_hand)
            print(f"The dealer's hand: {dealer_hand}")
            print(f"Your hand: {user_hand}")
        check_bust(user_hand)
        if check_bust(user_hand):
            print("Bust!")
            return
        if check_bust(user_hand) != "bust" or user_input == "s":
            print("The dealer is dealing their next card...")
            deal_card(dealer_hand)
            print(f"The dealer's hand: {dealer_hand}\nYour hand: {user_hand}")
        check_bust(dealer_hand)
        if check_bust(dealer_hand) == True:
            print("You win!")
        if user_input == "q":
            exit()

def help():
    pass

def main():
    pass

play_game()
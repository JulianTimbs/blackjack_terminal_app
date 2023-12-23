import random
import time
from colored import Style
from styles import style_dealerhand, style_userhand, style_announcement


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
        if check_card_available(card):
            user_hand.append(card)
        else:
            deal_card(user_hand)
    if hand == dealer_hand:
        if total_value(dealer_hand) < 17:
            if check_card_available:
                dealer_hand.append(card)
            else:
                deal_card(dealer_hand)
    return hand

def total_value(hand):
    i = 0
    total = 0
    for i in hand:
        total += i
    return total

def check_card_available(card):
    total = 0
    for value in user_hand:
        if value == card:
            total += 1
    for value in dealer_hand:
        if value == card:
            total += 1
    if total < 4:
         return True
    else:
         return False
    
def hit():
    deal_card(user_hand)
    deal_card(dealer_hand)
    print(f"{style_announcement}The dealer is dealing the cards...{Style.reset}")
    time.sleep(0.75)
    print(f"{style_dealerhand}The dealer's hand: {dealer_hand}{Style.reset}")
    time.sleep(0.75)
    print(f"{style_userhand}Your hand: {user_hand}{Style.reset}")

def stand():
    deal_card(dealer_hand)
    time.sleep(0.75)
    print(f"{style_dealerhand}The dealer's hand: {dealer_hand}{Style.reset}")
    time.sleep(0.75)
    print(f"{style_userhand}Your hand: {user_hand}{Style.reset}")
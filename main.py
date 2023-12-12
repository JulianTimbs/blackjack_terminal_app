import sys
import random

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

user_hand = [10, 10, 10]
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
        return "Bust"
    else:
        return "Under 21"
    
print(check_bust(user_hand))
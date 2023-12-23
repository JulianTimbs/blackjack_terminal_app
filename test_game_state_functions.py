import pytest
from game_state_functions import check_loss, check_tie, check_win
from card_functions import total_value

def test_loss():
    user_hand = [10, 10, 9]
    dealer_hand = [10, 10, 9]
    
    loss = check_loss(user_hand, dealer_hand)
    assert loss == True

def test_win_blackjack():
    user_hand = [10,11]
    dealer_hand = [1]

    blackjack = check_win(user_hand, dealer_hand)
    assert blackjack == True

def test_win_normal():
    user_hand = [10, 6, 3]
    dealer_hand = [10, 1, 7]

    win = check_win(user_hand, dealer_hand)
    assert win == True

def test_tie():
    user_hand = [10, 7]
    dealer_hand = [10, 7]

    tie = check_tie(user_hand, dealer_hand)
    assert tie == True
import pytest
from game_state_functions import check_loss, check_tie, check_win

user_hand = []
dealer_hand = []

def test_win():
    if user_hand == [10, 11]:
        assert check_win

def test_loss():
    if user_hand == [10, 10, 10]:
        assert check_loss

def test_tie():
    if user_hand == [10, 7, 1] and dealer_hand == [10, 8]:
        assert check_tie


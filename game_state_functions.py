from card_functions import total_value

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
    elif (total_value(dealer_hand) >= 17) and (total_value(user_hand) > total_value(dealer_hand)):
        print("You win!")
        return True

def check_loss(user_hand, dealer_hand):
    if total_value(dealer_hand) == 21:
        print("The dealer won...")
        return True
    if total_value(user_hand) > 21:
        print("Bust!")
        return True
    if (total_value(dealer_hand) >= 17 and total_value(dealer_hand) < 21):
        if total_value(dealer_hand) > total_value(user_hand):
            print("The dealer won...")
            return True

def check_tie(user_hand, dealer_hand):
    if total_value(dealer_hand) >= 17:
        if total_value(user_hand) == total_value(dealer_hand):
            print("It's a push!")
            return True
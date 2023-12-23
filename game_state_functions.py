from card_functions import total_value
from colored import Style
from styles import style_win, style_tie, style_loss

def check_win(user_hand, dealer_hand):
    if total_value(user_hand) == 21 and len(user_hand) == 2:
         print(f"{style_win}Blackjack!{Style.reset}")
         return True
    elif total_value(user_hand) == 21:
        print(f"{style_win}You win!{Style.reset}")
        return True
    elif total_value(dealer_hand) > 21:
        print(f"{style_win}You win!{Style.reset}")
        return True
    elif (total_value(dealer_hand) >= 17) and (total_value(user_hand) > total_value(dealer_hand)):
        print(f"{style_win}You win!{Style.reset}")
        return True

def check_loss(user_hand, dealer_hand):
    if total_value(dealer_hand) == 21:
        print(f"{style_loss}The dealer won...{Style.reset}")
        return True
    if total_value(user_hand) > 21:
        print(f"{style_loss}Bust!{Style.reset}")
        return True
    if (total_value(dealer_hand) >= 17 and total_value(dealer_hand) < 21):
        if total_value(dealer_hand) > total_value(user_hand):
            print(f"{style_loss}The dealer won...{Style.reset}")
            return True

def check_tie(user_hand, dealer_hand):
    if total_value(dealer_hand) >= 17:
        if total_value(user_hand) == total_value(dealer_hand):
            print(f"{style_tie}It's a push!{Style.reset}")
            return True
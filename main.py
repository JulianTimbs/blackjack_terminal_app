from errors import InvalidInputError, KeyboardInterrupt
from card_functions import deal_card, hit, stand, user_hand, dealer_hand
from game_state_functions import check_win, check_loss, check_tie
from bet_functions import get_bet, make_bet, update_running_total, get_running_total, update_highest_winnings, get_highest_winnings
from help import help
import time
from colored import Fore, Back, Style


def play_game():
    current_bet = 0
    running_total = int(get_running_total())
    print(f"Your running total is: ${running_total}")
    current_bet = get_bet()
    if current_bet == "\\quit":
        raise KeyboardInterrupt
    make_bet(current_bet)
    print("The dealer is dealing the cards...")
    time.sleep(0.75)
    while len(user_hand) < 2:
        deal_card(user_hand)
    deal_card(dealer_hand)
    print(f"The dealer's hand: {dealer_hand}")
    time.sleep(0.75)
    print(f"Your hand: {user_hand}")
    if check_win(user_hand, dealer_hand):
        running_total = running_total + (current_bet * 1.5) + current_bet
        running_total = int(running_total)
        update_running_total(running_total)
        print(f"Your running total is: ${running_total}")
        return
    while True:
        try:
            print(f"Your current bet is: ${current_bet}")  
            user_choice = input("Enter 'h' to hit or 's' to stand or 'd' to double down: ").lower()
            if user_choice not in ("h", "s", "d", "\\quit"):
                raise InvalidInputError
            if user_choice == '\\quit':
                raise KeyboardInterrupt
            if user_choice == "h":
                hit()
            if user_choice == "s":
                stand()
            if user_choice == "d":
                current_bet *= 2
                make_bet(current_bet)  
                hit()    
        except InvalidInputError:
            print("Invalid input") 
        if check_loss(user_hand, dealer_hand):
             running_total = running_total - current_bet
             update_running_total(running_total)
             print(f"Your running total is: ${running_total}")
             return
        if check_tie(user_hand, dealer_hand):
             print(f"Your running total is: ${running_total}")
             return
        if check_win(user_hand, dealer_hand):
             running_total = running_total + current_bet * 2
             update_running_total(running_total)
             print(f"Your running total is: ${running_total}")
             return       

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
    welcome = get_input(f"{Fore.black}{Back.white}{greeting}! Enter 'play' to start {text_insert} game of Blackjack or '\\quit' at anytime to quit the game or 'help' to see rules and terminology:{Style.reset} ")

def main():
    game_played = False
    greeting = "Welcome"
    text_insert = "a"
    running_total = 0 
    update_running_total(running_total)
    while True:
        try:
            get_running_total()
            start_prompt(greeting, text_insert)
            game_played = True
            greeting = "Hi again"
            text_insert = "another"
            play_game()
            user_hand.clear()
            dealer_hand.clear()
        except KeyboardInterrupt:
            if game_played:
                highest_winnings = int(get_highest_winnings())
                running_total = int(get_running_total())
                if running_total > highest_winnings:
                    update_highest_winnings(running_total)
                    print(f"New highest win! ${running_total}")
                    break
                else:
                    print(f"Your highest winnings is: ${highest_winnings}")
                print("Thanks for playing, see you next time!")
                break
            else:
                print("Ok, see you next time!")
                break
        except InvalidInputError:
            print("Invalid input")

main()

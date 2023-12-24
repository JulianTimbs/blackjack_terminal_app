from errors import InvalidInputError, KeyboardInterrupt
from card_functions import deal_card, hit, stand, user_hand, dealer_hand
from game_state_functions import check_win, check_loss, check_tie
from bet_functions import get_bet, make_bet, update_running_total, get_running_total, update_highest_winnings, get_highest_winnings, check_bets_file
from help import help
from styles import style_highscore, style_announcement, style_dealerhand, style_userhand, style_invalid, style_bet, style_runningtotal
from colored import Style
import time


def play_game():
    current_bet = 0
    running_total = int(get_running_total())
    current_bet = get_bet()
    make_bet(current_bet)
    print(f"{style_announcement}The dealer is dealing the cards...{Style.reset}")
    time.sleep(0.75)
    while len(user_hand) < 2:
        deal_card(user_hand)
    deal_card(dealer_hand)
    print(f"{style_dealerhand}The dealer's hand: {dealer_hand}{Style.reset}")
    time.sleep(0.75)
    print(f"{style_userhand}Your hand: {user_hand}{Style.reset}")
    if check_win(user_hand, dealer_hand):
        running_total = running_total + (current_bet * 1.5) + current_bet
        running_total = int(running_total)
        update_running_total(running_total)
        return
    while True:
        try:
            print(f"{style_bet}Your current bet is: ${current_bet}")
            user_choice = input(
                f"{style_announcement}Enter 'h' to hit or 's' to stand or 'd' to double down: {Style.reset}").lower()
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
            print(f"{style_invalid}Invalid input{Style.reset}")
        if check_loss(user_hand, dealer_hand):
            running_total = running_total - current_bet
            update_running_total(running_total)
            return
        if check_tie(user_hand, dealer_hand):
            return
        if check_win(user_hand, dealer_hand):
            running_total = running_total + current_bet * 2
            update_running_total(running_total)
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
    welcome = get_input(
        f"{style_announcement}{greeting}! Enter 'play' to start {text_insert} game of Blackjack or '\\quit' at anytime to quit the game or 'help' to see rules and terminology: {Style.reset}")


def main():
    game_played = False
    greeting = "Welcome"
    text_insert = "a"
    running_total = 0
    check_bets_file()
    update_running_total(running_total)
    while True:
        try:
            start_prompt(greeting, text_insert)
            game_played = True
            greeting = "Hi again"
            text_insert = "another"
            play_game()
            running_total = get_running_total()
            print(
                f"{style_runningtotal}Your running total is: ${running_total}{Style.reset}")
            user_hand.clear()
            dealer_hand.clear()
        except KeyboardInterrupt:
            if game_played:
                highest_winnings = int(get_highest_winnings())
                running_total = int(get_running_total())
                if running_total > highest_winnings:
                    update_highest_winnings(running_total)
                    print(
                        f"{style_highscore}New highest win! ${running_total}{Style.reset}")
                    break
                else:
                    print(
                        f"{style_announcement}Your highest winnings is: ${highest_winnings}{Style.reset}")
                print(
                    f"{style_announcement}Thanks for playing, see you next time!{Style.reset}")
                break
            else:
                print(f"{style_announcement}Ok, see you next time!{Style.reset}")
                break
        except InvalidInputError:
            print(f"{style_invalid}Invalid input{Style.reset}")


main()

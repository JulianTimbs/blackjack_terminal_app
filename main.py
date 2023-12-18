from errors import InvalidInputError, KeyboardInterrupt
import sys
import random
import csv
import time

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
    if hand == user_hand:
        for i in user_hand:
            total += i
        return total
    if hand == dealer_hand:
        for i in dealer_hand:
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

def get_bet():
    while True:
        try:
            user_bet = input("Input your bet amount: ")
            if user_bet == "\\quit":
                raise KeyboardInterrupt
            user_bet = int(user_bet) # So user can still quit during bet prompt
            if user_bet < 0:
                raise ValueError        
            break
        except ValueError:
            print("Bet must be a positive number")
        except InvalidInputError:
            print("Invalid input")
    return user_bet      

def make_bet(new_bet):
    bets = []
    with open('bets.csv', mode='r', newline='') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            bets.append(row)   
    for row in bets:
        row['Current Bet'] = new_bet
        break
    with open('bets.csv', mode='w', newline='') as f:
        fieldnames = ['Current Bet', 'Running Total', 'Highest Winnings']
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()
        for row in bets:
            csv_writer.writerow(row)

def update_running_total(running_total):
    bets = []
    try:
        with open('bets.csv', mode='r', newline='') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                bets.append(row)   
        for row in bets:
            row['Running Total'] = running_total
            break
        with open('bets.csv', mode='w', newline='') as f:
            fieldnames = ['Current Bet', 'Running Total','Highest Winnings']
            csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
            csv_writer.writeheader()
            for row in bets:
                csv_writer.writerow(row)
    except FileNotFoundError:
        with open('bets.csv', mode='w', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['Current Bet', 'Running Total', 'Highest Winnings']) 
            csv_writer.writerow([0, 0, 0])

def get_running_total():
    bets = []
    running_total = 0
    with open('bets.csv', mode='r', newline='') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            bets.append(row)   
    for row in bets:
        running_total = row['Running Total']
        return running_total

def get_highest_winnings():
    bets = []
    with open('bets.csv', mode='r', newline='') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            bets.append(row)   
    for row in bets:
        highest_winnings = row['Highest Winnings']
        return highest_winnings

def update_highest_winnings(highest_winnings):
     bets = []
     with open('bets.csv', mode='r', newline='') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            bets.append(row)   
        for row in bets:
            row['Highest Winnings'] = highest_winnings
            break
     with open('bets.csv', mode='w', newline='') as f:
        fieldnames = ['Current Bet', 'Running Total','Highest Winnings']
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()
        for row in bets:
            csv_writer.writerow(row)

def hit():
    deal_card(user_hand)
    deal_card(dealer_hand)
    print("The dealer is dealing the cards...")
    time.sleep(0.75)
    print(f"The dealer's hand: {dealer_hand}")
    time.sleep(0.75)
    print(f"Your hand: {user_hand}")

def stand():
    deal_card(dealer_hand)
    time.sleep(0.75)
    print(f"The dealer's hand: {dealer_hand}")
    time.sleep(0.75)
    print(f"Your hand: {user_hand}")

def play_game():
    current_bet = 0
    running_total = int(get_running_total())
    print(f"Your running total is: {running_total}")
    current_bet = get_bet()
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
        update_running_total(running_total)
        print(f"Your running total is: {running_total}")
        return
    while True:
        try:
            print(f"Your current bet is: {current_bet}")  
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
             print(f"Your running total is: {running_total}")
             return
        if check_tie(user_hand, dealer_hand):
             print(f"Your running total is: {running_total}")
             return
        if check_win(user_hand, dealer_hand):
             running_total = running_total + current_bet * 2
             update_running_total(running_total)
             print(f"Your running total is: {running_total}")
             return
        


def help():
    print("The objective:\nThe goal is to beat the dealer by having a hand value closer to 21 without exceeding it.\n\nCard Values:\nNumbered cards are valued at their face value\nFace cards are worth 10\nAces can be worth 11 or 1 whichever is most beneficial\n\nBasic Gameplay:\nDeal: The player and dealer are dealt two cards\nHit: The player can choose to take (hit) additional cards\nStand: The player can choose to keep their current hand (stand) and not receive anymore cards\nBust: If a hand exceeds 21 points, it busts and is a losing hand.\n\nWinning and losing:\nIf the player's hand is closer to 21 than the dealer's without busting, the player wins.\nIf the dealer busts, all remaining players win.\nIf both the player and the dealer have the same total, it's a push (tie), and the player's bet is returned.\nA 'Blackjack' is a hand with an Ace and a 10-value card, totaling 21. It usually pays out more than a regular win.\n\nDealer's Play:\nThe dealer hits until their hand is 17 or higher and stands otherwise.\n\nTerminology:\nHit: To take another card.\nStand: To keep the current hand and end the turn.\nBust: To exceed 21 points and lose the round.\nPush: A tie between the player and the dealer, resulting in the return of the player's bet.\nBlackjack: A hand with an Ace and a 10-value card, totaling 21.\nDouble Down: To double the original bet and receive exactly one more card.\n")

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
    welcome = get_input(f"{greeting}! Enter 'play' to start {text_insert} game of Blackjack or '\\quit' at anytime to quit the game or 'help' to see rules and terminology: ")

def main():
    greeting = "Welcome"
    text_insert = "a"
    running_total = 0 
    update_running_total(running_total)
    while True:
        try:
            get_running_total()
            start_prompt(greeting, text_insert)
            greeting = "Hi again"
            text_insert = "another"
            play_game()
            user_hand.clear()
            dealer_hand.clear()
        except KeyboardInterrupt:
            highest_winnings = int(get_highest_winnings())
            running_total = int(get_running_total())
            if running_total > highest_winnings:
                update_highest_winnings(running_total)
                print(f"New highest win! {running_total}")
                print("Thanks for playing, see you next time!")
                break
            else:
                print(f"Your highest winnings is: {highest_winnings}")
                print("Thanks for playing, see you next time!")
                break
        except InvalidInputError:
            print("Invalid input")

main()

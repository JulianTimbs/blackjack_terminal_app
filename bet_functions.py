import csv
from colored import Style
from styles import style_invalid, style_bet, style_announcement, style_highscore

bets = []


def get_bet():
    while True:
        try:
            user_bet = input(f"{style_bet}Input your bet amount: $")
            if user_bet == "\\quit":
                raise KeyboardInterrupt
            # So user can still quit during bet prompt
            user_bet = int(user_bet)
            if user_bet < 0:
                raise ValueError
            break
        except ValueError:
            print(f"{style_invalid}Bet must be a positive number{Style.reset}")
        except KeyboardInterrupt:
            highest_winnings = int(get_highest_winnings())
            running_total = int(get_running_total())
            if running_total > highest_winnings:
                update_highest_winnings(running_total)
                print(
                    f"{style_highscore}New highest win! ${running_total}{Style.reset}")
                exit()
            else:
                print(
                    f"{style_announcement}Your highest winnings is: ${highest_winnings}{Style.reset}")
            print(f"{style_announcement}Ok, see you next time!{Style.reset}")
            exit()
    return user_bet


def read_bets_file():
    bets.clear()
    with open('bets.csv', mode='r', newline='') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            bets.append(row)


def write_to_bets_file():
    with open('bets.csv', mode='w', newline='') as f:
        fieldnames = ['Current Bet', 'Running Total', 'Highest Winnings']
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()
        for row in bets:
            csv_writer.writerow(row)


def make_bet(current_bet):
    read_bets_file()
    for row in bets:
        row['Current Bet'] = current_bet
        break
    write_to_bets_file()


def update_running_total(running_total):
    read_bets_file()
    for row in bets:
        row['Running Total'] = running_total
        break
    write_to_bets_file()


def get_running_total():
    running_total = 0
    read_bets_file()
    for row in bets:
        running_total = row['Running Total']
    return running_total


def get_highest_winnings():
    read_bets_file()
    for row in bets:
        highest_winnings = row['Highest Winnings']
    return highest_winnings


def update_highest_winnings(highest_winnings):
    read_bets_file
    for row in bets:
        row['Highest Winnings'] = highest_winnings
        break
    write_to_bets_file()


def check_bets_file():
    try:
        with open('bets.csv', mode='r', newline='') as f:
            return
    except FileNotFoundError:
        with open('bets.csv', mode='w', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(
                ['Current Bet', 'Running Total', 'Highest Winnings'])
            csv_writer.writerow([0, 0, 0])

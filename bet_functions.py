import csv
from errors import InvalidInputError

def get_bet():
    while True:
        try:
            user_bet = input("Input your bet amount: $")
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
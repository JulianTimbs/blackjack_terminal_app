def help():
    print("""
          The objective:\nThe goal is to beat the dealer by having a hand value 
          closer to 21 without exceeding it.\n\nCard Values:\nNumbered cards are 
          valued at their face value\nFace cards are worth 10\nAces can be worth 
          11 or 1 whichever is most beneficial\n\nBasic Gameplay:\nDeal: The 
          player and dealer are dealt two cards\nHit: The player can choose to 
          take (hit) additional cards\nStand: The player can choose to keep their 
          current hand (stand) and not receive anymore cards\nBust: If a hand exceeds 
          21 points, it busts and is a losing hand.\n\nWinning and losing:\nIf the 
          player's hand is closer to 21 than the dealer's without busting, the 
          player wins.\nIf the dealer busts, all remaining players win.\nIf both 
          the player and the dealer have the same total, it's a push (tie), and 
          the player's bet is returned.\nA 'Blackjack' is a hand with an Ace and 
          a 10-value card, totaling 21. It pays out more than a regular win.\n\n
          Dealer's Play:\nThe dealer hits until their hand is 17 or higher and 
          stands otherwise.\n\nTerminology:\nHit: To take another card.\n
          Stand: To keep the current hand and end the turn.\nBust: To exceed 21 
          points and lose the round.\nPush: A tie between the player and the dealer, 
          resulting in the return of the player's bet.\nBlackjack: A hand with an 
          Ace and a 10-value card, totaling 21.\nDouble Down: To double the original 
          bet and receive exactly one more card.\n
          """)

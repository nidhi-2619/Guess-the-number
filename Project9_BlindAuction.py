import os

def clear():
    
    _var = os.system('cls')

def bids_winner(bids):
    highest_bid = 0
    for bidder in candidates:
        bid_money = candidates[bidder]
        if bid_money > highest_bid:
            highest_bid = bid_money
            winner = bidder
    print(f"The winner is {winner} with bid ${highest_bid}")        

candidates = {}
auction_end = False
while not auction_end:
    name  = input("What is your name?")
    bid = int(input("What is your bid? $"))
    candidates[name] = bid
    ask = input("Are there any other bidder?Type 'YES' or 'NO' ").upper()
    if ask == "YES":
        clear()
        
    else:
        auction_end = True
        bids_winner(candidates)



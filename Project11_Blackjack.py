#blackjack
import random
def blackjack():
    ask = input("Do you want to blackjack?Type 'Y' for yes and 'N' for no ").upper()
    if ask == 'Y':
        Game()
    else:
        exit(0)    
def Game():
    
    def deal_cards():
        """"Returns random card from the deck"""
        deck_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        card = random.choice(deck_cards)
        return card
    cards = deal_cards()
    player_cards = []
    for _ in range(0,2):
        player_cards.append(random.randint(2,12))
    print("Player cards:", player_cards,"Your score is",sum(player_cards))
    computer_cards=[cards]
    print("Computer cards:", computer_cards)
    def user_score(player_score):
        if sum(player_score) == 21 and len(player_score) == 2:
            return 0
        elif sum(player_score)<21 :
            play(player_cards,computer_cards)
            return sum(player_score)
        else:
            return sum(player_score)
    user = user_score(player_cards)    
    def dealer_score(computer_score):
        sum(computer_score)
        if sum(computer_score) == 21 and len(computer_score)==2:
            return 0
        elif sum(computer_score)>21 and len(computer_score)==2:
            computer_cards.remove(11)
            computer_cards.append(1)
        elif sum(computer_score)>21:
            return sum(computer_score)    
        else:
            while sum(computer_score)<=17:
                computer_cards.append(random.randint(2,12))
    dealer = dealer_score(computer_cards)            
    def compare(user,dealer):
        if sum(user) == sum(dealer):
            print("Draw")
            blackjack()
        elif sum(user) > sum(dealer):
            print("The Dealer busted, You won")
            blackjack()
        elif sum(user) < sum(dealer):
            print("Ops You busted,The Dealer Won")
            blackjack() 
    def play(player_score,computer_score):
        continue_playing = True
        while continue_playing:
            choice = input("Do you want another card? Type 'Y' for yes and 'N' for pass: ").upper()
            if choice == "Y":
                player_cards.append(random.randint(2,12))
                print("Player cards:", player_cards,"Your score is",sum(player_cards))
                user_score(player_score)
            else:
                continue_playing = False
                dealer_score(computer_score)       
                               
    
blackjack()

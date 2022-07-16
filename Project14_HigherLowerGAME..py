import Game_Data_Project14
import os
def clear():
    
    _var = os.system('cls')
import random
Player1 = random.randint(0,len(Game_Data_Project14.data)-1)
Player2 = random.randint(0,len(Game_Data_Project14.data)-1)
computer = Game_Data_Project14.data[Player1]
opponent = Game_Data_Project14.data[Player2]
score = 0
correct = True
print(Game_Data_Project14.logo)
while correct:
    
    Player1 = Player2
    computer = Game_Data_Project14.data[Player1]
    print(Game_Data_Project14.data[Player1]['name'],end=", ")
    print("A " + Game_Data_Project14.data[Player1]['description'],end=", ")
    print("from " + Game_Data_Project14.data[Player1]['country'])
        
    print(Game_Data_Project14.vs)

    Player2 = random.randint(0,len(Game_Data_Project14.data)-1)
    opponent = Game_Data_Project14.data[Player2]
    print(Game_Data_Project14.data[Player2]['name'],end=", ")
    print("A " + Game_Data_Project14.data[Player2]['description'],end=", ")
    print("from " + Game_Data_Project14.data[Player2]['country'])
    choice = input("Who have more followers ? Enter Your Choice A or B? ").upper()
    if choice == "A" and computer['follower_count']> opponent['follower_count']: #that is chooses computer  
            correct = True            
            score +=1
            clear()
            print("You are right! Your current score is: ",score)
            
            
            
    elif choice == "B" and computer['follower_count']<opponent['follower_count']:
            correct = True
            score +=1
            clear()
            print("You are right! Your current score is: ",score)
        
            
    elif  choice == "A" and computer['follower_count']<opponent['follower_count']:
            correct =False
            print("Sorry,You are wrong! Your final score is: ",score)
            exit(0)
    else:
        correct = False
        print("Sorry,You are wrong! Your final score is: ",score)
        exit()
            


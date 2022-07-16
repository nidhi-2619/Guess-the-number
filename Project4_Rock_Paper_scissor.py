# rock paper scissor game
import random

game = ["✊🏻","✋🏻","✌️"]
print(game)
choice = input("Enter\n 1 for rock\n 2 for paper\n 3 for scissor\n")
if choice == 1:
    choice = "✊🏻"
elif choice == 2:
    choice = "✋🏻"
else:
    choice = "✌️"

print("Computer choose")
cmp_choose  = random.choice(["✊🏻","✋🏻","✌️"])
print(cmp_choose + "\nYou choose")

if cmp_choose == "✊🏻" and choice == "✋🏻":
    print(f"{choice}\nYou won")
elif cmp_choose == "✊🏻" and choice == "✌️":
    print(f"{choice}\nYou lose")
elif cmp_choose == "✋🏻" and choice == "✊🏻":
    print(f"{choice}\nYou won")
elif cmp_choose == "✋🏻" and choice == "✌️":
    print(f"{choice}\nYou lose")
elif cmp_choose == "✌️" and choice == "✋🏻":
    print(f"{choice}\nYou won")
elif cmp_choose == "✌️" and choice == "✊🏻":
    print(f"{choice}\nYou lose")
else:
    print("Its a Draw")
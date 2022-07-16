from typing import Counter

print("Welcome to the rollecoaster!")
height = int(input("What is your height in cm?"))
if height >= 150:
    print("You can go!")
else:
    print("You cannot go!")

# interactive coding
# check even or odd
print("Enter the number you want to check")
num = int(input())
if num % 2 == 0:
    print("This number is an even number")
else:
    print("This number is an odd number")

# nested if else       
print("Welcome to the waterslide!")
height = int(input("What is your height?"))

if height >= 120:
    print("You can have a go !")
    age = int(input("What is your age?"))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("You cannot have a go!")

# interactive coding
# pizza order         

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

# interactive coding
# love calculator
print("Welcome to the love calculator")
name1 = input("Enter your name: ")
name2 = input("Enter your partner's name: ")

couple_name = name1 + name2
couple_name = couple_name.upper()

T = couple_name.count("T")
R = couple_name.count("R")
U = couple_name.count("U")
E = couple_name.count("E")

L = couple_name.count("L")
O = couple_name.count("O")
V = couple_name.count("V")
E = couple_name.count("E")

true = T + R + U + E
love = L + O + V + E
love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score},You are compatible")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score},You guys are alright")
else:
    print(f"Your score is {love_score}")

# interactive coding  
# leap year         
year = int(input("Enter the year you want to check: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not a Leap year.")
    else:
        print("Leap year.")

else:
    print("Not a leap year.")

import random
logo = """
   ___                       _   _                                  _                
  / _ \_   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __  
 / /_\/ | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__| 
/ /_\\| |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |    
\____/ \__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|                                                                                     
                                                                                     
"""
print(logo)
difficulty_level = input("Choose the difficulty.Type 'easy' or 'hard': ").lower()
number = random.randint(1,101)

def game(num,attempt):
    "Return the result for easy difficulty"
    while attempt !=0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if num == guess:
            return f"you got it ! The number is {num}"
        elif num < guess:
            print('Too high.\nGuess again')
        else:
            print('Too low.\nGuess again')
        attempt -=1
    if attempt == 0:
        return f"Oops ! You are out of attempts ,the number was {num}"

if difficulty_level == 'easy':
    attempts = 10
    result = game(number,attempts)
    print(result)

else:
    attempts = 5
    result = game(number,attempts)
    print(result)





#Step 1 
import random
import hangman_art
import hangman_words
word_list = hangman_words.word_list
lives = 6
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
print(hangman_art.logo)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
for _ in chosen_word:# when we are not doing anything with the variable in loop we can take _ as variable
      display+='_' # for eg  for _ in list_name:
print(display)
# The end parameter in the print function is used to add any string. At the end of the output of the print statement in python. By default, the print function ends with a newline. Passing the whitespace to the end parameter (end=' ') indicates that the end character has to be identified by whitespace and not a newline.    
end_of_game = False
while not end_of_game:   
      guess = input("Guess a letter\n").lower()
      for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                  display[position]=letter
      if guess not in chosen_word:
            lives -=1
            print(f"The guessed letter is not present in the word\n Your life left:{lives} ")
            print(hangman_art.stages[lives])
            if  lives == 0 :
                  end_of_game = True
                  print("You lose")        
      print(f"{' '.join(display)}")
      
      if "_" not in display:
            end_of_game = True
            print("You win")
# the in keyword is basically use to check if the particular element exist in the list 
print(hangman_art.stages[lives])
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8BA,  ,ADPPPPP88 88          
"8A,   ,AA 88,    ,88 "8B,   ,AA AA    ]8I 88,    ,88 88          
 `"YBBD8"' `"8BBDP"Y8  `"YBBD8"' `"YBBDP"' `"8BBDP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,ADPPYBA, 88 8B,DPPYBA,  88,DPPYBA,   ,ADPPYBA, 8B,DPPYBA,  
A8"     "" 88 88P'    "8A 88P'    "8A A8P_____88 88P'   "Y8  
8B         88 88       D8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']


def caesar(start_text,shift_number,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_number *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)    
            new_position = position + shift_number
            end_text += alphabet[new_position]
        else:
            end_text += letter    
    print(f"Here's the {cipher_direction}d result: {end_text}")
        
should_end = False
while not should_end:
    direction = input("Type encode for encryption and decode for decryption\n")
    text = input("Type the text message\n").lower()
    shift = int(input("Type shift number\n"))
    shift = shift%26
    caesar(start_text=text,shift_number=shift,cipher_direction=direction) ;   
    restart = input("Do you wanna encode and decode again")
    if restart == "no":
        should_end = True  
        print("Goodbye !")
    
    
    
            
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1
#   for char in start_text:
#     #TODO-3: What happens if the user enters a number/symbol/space?
#     #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#     #e.g. start_text = "meet me at 3"
#     #end_text = "•••• •• •• 3"
#     if char in alphabet:
#       position = alphabet.index(char)
#       new_position = position + shift_amount
#       end_text += alphabet[new_position]
#     else:
#       end_text += char
#  
# #TODO-1: Import and print the logo from art.py when the program starts.
# # from art import logo
# print(logo)

# #TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# #e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# #If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# #Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
# should_end = False
# while not should_end:

#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))
#   #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#   #Try running the program and entering a shift number of 45.
#   #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#   #Hint: Think about how you can use the modulus (%).
#   shift = shift % 26

#   caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#   restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#   if restart == "no":
#     should_end = True
#     print("Goodbye")
    




          
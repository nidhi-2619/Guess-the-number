#Password Generator
import random
letters = ["a", "b", "c", "d", "e","f", "g", "h", "i", "j", "i","k", "l", "m", "n", "o", "p","q","r", "s", "t", "u", "v","w", "x", "y", "z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","(",")","@","#","$","*","&","/","^","%","+"]
print("Welcome to Password Generator")
n_letters = int(input("How many letters do you want in your password?"))
n_numbers = int(input("How many numbers do you want in your password?"))
n_symbols = int(input("How many symbols do you want in your password?"))

password =[]
for i in range(1,n_letters):
    password += random.choice(letters)
for j in range(1,n_numbers):
    password += random.choice(numbers)    
for ij in range(1,n_symbols):
    password += random.choice(symbols)  
x = random.shuffle(password)
gen_ps = ""
for rev in password:
    gen_ps += rev
print(gen_ps)    
    
   
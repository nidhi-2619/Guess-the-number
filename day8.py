#function and arguments
# arguments are of two types Positional arguments and keywords arguments 
# positional arguments are depend on position of arguments pass on the function
# keyword arguments are passed with assigned value ,so the position doesnt matter
# positonal arguments eg.
def greet(name,age):
    print(f"Hi,{name}")
    print(f"I am {age} years old.")
    
greet("Nidhi",19)    
# keyword arguments eg.
def greet(name,age):
    print(f"Hi,{name}")
    print(f"I am {age} years old.")
    
greet(age=19,name="Aditi")  

# math.floor round down the number 
# math.ceil round up the number
import math
def paint_calc(width,height,cover):
     no_of_cans = math.ceil((width*height)/cover)
     print(f"You'll need {no_of_cans} cans of paint")    

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


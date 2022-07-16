# randomization in python
import random #by using import we can use the random module
print("print a number")
choose = random.randint(100,300)#here basically a range we specifying
print(choose)
# module are basically python files and import function is used to insert a python file into another
#how to create a python module ,just simply create a file and import in into the main file 
#how to use it in the python code ,the syntax is modulename.function you want to use from the module 
# we can increase the range of floating point no by multiplying it with a number,range of floating point number is [x,y)
love_score = input("Enter your and yours partner: ")
love_score = random.randint(1,100)
print(love_score)

# list is just a set of square brackets in which items are stored.This item can be of any data type or 
# mixed data types
# why is the first item is at zero?
# it is basically shift or offset from the beginning so first item at so shift so 
# it is zero while second item is shifted by one so it's index is 1 and so on.
# we can use negative index also it means the list start counting from the end of the list
# to change the item in the list just perform:
# item_name[index_no] = "changed"
friends =["Aditi","Ayush","Nidhi"]
print(friends[2])
# append function is used to add an item in the end of the list
# extend function is used to add lot of items in the end of the list
friends.append("Nandini")
print(friends)

# the len function gives the length of the list or number of characters in the string

# interactive coding
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#split string method is used to convert the string into a list if no argument is passed split take whitespace as argument

x = len(names)
print(names[random.randint(0,x - 1)] + " is going to buy the meal today!")
#in python the matrix is readed as column and row that is 31 is column 3 and row 1 

# interactive coding
# TREASURE MAP
row1 = ["😋","😋","😋"]
row2 = ["😋","😋","😋"]
row3 = ["😋","😋","😋"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to mark?")

column = int(position[0])
row = int(position[1])
map[column-1][row-1]="😛"

print(f"{row1}\n{row2}\n{row3}")

# for randomly choosing from a list we use random.choice

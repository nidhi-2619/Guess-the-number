# loops
# for loop 
# for item in list_of_items: here we give the name to the single item to go through the loop
# do something in the list
fruits = ["apple","orange","pear"]
for fruit in fruits:
    print(fruit)
    #  what is actually happening here is for each time fruit names are assigned to the variable fruit 
# this is used for list only   
# now to use loop independentLy we use range function
# syntax would be for i in range(a,b) where i will be fromm a to b  not including b [a,b)
# normally range function th evalue increase by +1 but if you want to increase by any other no then the syntaxing would be range(a,b,c) where c is used to define the increase in no.

# shuffle function is used to shuffle in list
# list slicing is performed like [3:5][ inclusive:exclusive]
# [:5] means start from 0 to 4
# [2: ]means start from 2 to last
# if x is a list 
# y = x 
# both the list pointing to same list ,so changes made in y will reflect in x
#  to avoid this we have to define x explicitly like 
# y = list(x)
# or  y =x[:]

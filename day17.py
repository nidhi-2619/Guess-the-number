# class
# syntax of class is 
class User:
    pass # pass is used to overcome the indentation error when we dont want to put anything in 
# constructor it is used to create attributes for the object
# in python __init__ is a constructor 
# These are attributes
    def __init__(self,user_id,username):
        self.id=user_id # here self is used for object that has been created
        self.username=username
        self.followers = 0
        self.following = 0
    def follow(self,user): #this is method   
        user.followers +=1  #user is parameter
        self.following +=1 #here self is used for object syntax is self(object).attribute
        
user_1 = User("001","Nidhi")       
user_2 = User("002","Aditi")        

# syntax for attribute is object.attribute 
print(user_1.username)
user_1.follow(user_2) #method syntax is object.method(object two as argument )
print(user_1.following)
print(user_1.followers)
        
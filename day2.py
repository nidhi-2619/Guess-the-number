#type int do not have any length so it will create type error
#DATA TYPE
#string type
#String is basically a set of characters which can be access by index value [] that start with 0
#number inside a string does not count as integer since anything inside double quote is consider as String

print("This is a string")

#integer type
#simple number in a programming lingo is integer and larger no 123,456,789  written as 123_456_789 so it 
# so it convert it into like 123456789
print(123+445)
print(123_456_778)

# float TYPE
# the decimal values are the float values
print(3.141592653589)

# Boolean TYPE
# it has only two possible values TRUE and FALSE true is for 1 and false is for 0
bool = True

#type function is used check the datatype
# we cannot concatenate string with an integer ,it will error so we have to do type conversion 

# interactive coding 
sum_of_digit = input("Enter the number:") #string type
first_digit = int(sum_of_digit[0]) #string to integer
second_digit = int(sum_of_digit[1]) #string to integer
result = first_digit + second_digit
print(result)

#mathematical operation
# the result of / operator is always floating point number so we have to do type conversion for int result
# double astriks ** is used for power
# PEMDAS  () ** */ +- L to R
print(3 * 3 + 3 / 3 - 3  )
print(3 * (3 + 3) / 3 - 3  )

# BMI calculator
height = float(input("Enter your height:"))
weight = float(input("Enter your weight:"))

BMI = weight/(height**2)
print(int(BMI))

# round function is used to round of the decimal value it can be used for changing float to int without using type conversion
# with the help of round function we can specify the decimal value by round( operation , specify decimal value)
print(round(9/2,2))
# floor division can also be used to chop off the values of the decimal values and give int 
print(9//2)

# f- string help to include variable without concatenation (f"string {variable}) it also handy
# as we dont have to change the data type repeatedly
score = 0 
# f-string 
print(f"Your score is {score}")




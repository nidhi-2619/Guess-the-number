# function with output

def format_name(f_name,l_name):
   f_name= f_name.title() #the title function capitalize first letter of every word
   l_name= l_name.title()
   print (f_name,l_name)

candidate = format_name("nidhi","nishad") 
print(candidate)
# title changes the first alphabetic character in every group of alphabetic characters to a capital and the rest of each group to lower.

# capitalize only changes the first alphabetic character if it is at the beginning of the string to a capital and the rest to lower.
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
             return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    """ This give the no of days present in a particular month when year and month is passed as arguments"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap(year) and month == 2:
        return 29
    return month_days[month-1]
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# Docstring is basically a piece of text that we add in our function which explain what the funtion actually does
# syntax is triple quotation and written just after the function





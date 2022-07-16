# Calculator
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def addition(n1, n2):
    """return the sum of two numbers"""
    return n1 + n2


def subtraction(n1, n2):
    """return the difference"""
    return n1 - n2


def divide(n1, n2):
    """return the quotient """
    return n1 / n2


def multiply(n1, n2):
    """return the product"""
    return n1 * n2


operations = {"+": addition,
              "-": subtraction,
              "*": multiply,
              "/": divide,
              }
def calculator():
    print(logo)
    n1 = float(input("Enter the first number "))
    for operate in operations:
        print(operate)

    should_continue = True

    while should_continue:
        choice = (input("Pick an operator: "))
        n2 = float(input("Enter the next number: "))
        calculation_function = operations[choice]
        ans = calculation_function(n1, n2)
        print(f"{n1} {choice} {n2} = {ans}")
        
        ask = input("Type 'y' to continue the calculation {ans} or 'n' to start over the calculation").lower()
        
        if ask == 'y':
            num1 = ans
        else:
            should_continue = False
            calculator()
            
calculator()
        
        
        

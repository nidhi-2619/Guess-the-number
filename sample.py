# mytuple = ("apple","banana","cherry")
# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# # factorial
# def fact(n):
#     if n<=1:
#         return 1;
#     else:
#         return n*fact(n-1)
    
# num = int(input())
# factorial = fact(num)
# print(factorial)
    
    
# # fibonacci series
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
    
    
# num = int(input())
# for i in range(num):
#     fib_series = fib(i)
#     print(fib_series)
    
#  sum pf first n natural numbers
def sum(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum
    
num = int(input())
print(sum(num))

    
# tower of hanoi


input1 = ['a','b','c']
input2 = ['b','c']
sm = 0
for i in input1:
    if i in input2:
        sm += ord(i)
n = len(str(sm))
tot = 0 
while n>1:
    s = str(sm)
    list_num = list(map(int,s.strip()))
    tot = sum(list_num)
    n = len(str(tot))    
print(tot)    
x=1
y=1
z=0
d=0
count=0
a=int(input("enter your number :"))
b=int(input("eneter your number :"))
while True:
    count+=1
    x=y
    y=z
    z=x+y
    if z%a==0:
        d+=1
    if d==b:
        break
print(count)
    
        
        

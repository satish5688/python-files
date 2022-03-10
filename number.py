#### prime Number
c=int(input('enter your Number :'))
a=1
while a<c:
    b=2
    while b<a:
        if a%b==0:
            break
        b+=1
    else:
        print(a)
    a+=1






####### febonci series

# a=int(input("up to how much you need febonnci numbers :"))
# x=0
# y=1
# z=1
# counter = 0
# while z<a:
#     print(z)
#     x=y
#     y=z
#     z=x+y
#     counter+=1
# print("Between 1 to", str(a),"there is ",counter, "ficonacci numbers.")



# ### 2) ARMSTRONG NUMBERS

# d=1
# counter=0
# a=int(input("up to how much you need amstrong numbers :"))
# while a>=d:
#     l=len(str(d))
#     e=d
#     c=0
#     while e>0:
#         b=e%10
#         e=e//10
#         c+=b**l
#     if c==d:
#         print(c)
#         counter+=1
#     d+=1
# print("there is ",counter,"Amstrong numburs betwee 1 to",a)



# #  ## 3) HAPPY NUMBERS
# c=int(input("Enter Num:"))
# s=0
# for a in range(1,c+1):
#     f = a
#     while True:
#         total = 0
#         while a>0:
#             b=a%10
#             a = a//10
#             total += b*b
#         a=total
#         if total == 1:
#             print(f)
#             s+=1
#             break
#         if a == 4:
#             break
# print("** form 1 to",str(c),"there is",s,"Happy numbers that is given above")



### 4) Harshad Numbers
# n=int(input('up to how much you want harshad numbers : '))
# s=0
# for i in range(1,n+1):
#     sum=0
#     h=i
#     while i>0:
#         r=i%10
#         sum+=r
#         i=i//10
#     if h%sum==0:
#         print(h)
#         s+=1
# print("from 1 to",n,"there is",s,"harshad numbers that is given above.")

# a=int(input("up to how much you need Harshad numbers :"))
# s=0
# for i in range(1,a+1):
#     st = str(i)
#     total = 0
#     for j in st:
#         total+=int(j)
#     if i/total == i//total:
#         print(i)
#         s+=1
# print("from 1 to",a,"there is",s,"Harshad numbers that is given above.")



## 5) PERFECT NUMBERS

# a=int(input('up to how much you want perfect no.: '))
# s=0
# for g in range(1,a+1):
#     per=0
#     for i in range(1,g):
#         if g%i==0:
#             per+=i
#     if g==per:
#         print(g)
#         s+=1
# print("from 1 to",a,"there is",s,"perfect numbers that is give above")



# ### strong number
# a=1
# s=int(input("enter your number :"  ))
# while a<=s:
#     b=a
#     c=a
#     e=0
#     while c>0:
#         x=c%10
#         c//=10
#         d=1
#         while x>0:
#             d*=x
#             x-=1
#         e+=d
#     if b==e:
#         print(e)
#     a+=1




### print prime numbers up to input by one loop

# a=2
# b=1
# c=0
# s=int(input("enter your number :"))
# while a<=s:
#     if a%b==0:
#         c+=1
#     if b>a:
#         if c==2:
#             print(a)
#         a+=1
#         b=1
#         c=0
#     else:
#         b+=1
# print("this is your all prime numbers from 1 t0",s)  




# integer,string,f=0,0,0
# b=[]
# a=[1,2,22,34,24,56,65,55,67,"satish"," roshan",27.9,"akash",34.5,78,"pratik",3.9, 4.5,23,45,"prakash"]
# for s in a:
#     if type(s)==int:
#         integer+=1
#         c=a.remove(s)
#         b.append(c)
#     elif type(s)==float:
#         f+=1
#     elif type(s)==str:
#         string+=1
# print(b)



    
 
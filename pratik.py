# a = "abcdefghijklmnopqrstuvwxyz" 
# c=a[::-1]
# print(c)

# a = "My name is Apple"
# b=a.find("Apple")
# c=a[::-1]
# print(c)

# a = "First and Second" 
# f=a[:6]
# s=a[10:]
# print(f,s)

# a = "rahulsa"
# b=len(a)//2
# c=a[:b]
# d=a[b:]
# print(c)
# print(d)


# a = "abcdefghijklmnopqrstuvwxyz"
# c=a.replace("",",")
# print(c)
# d=a.replace("","|")
# print(d)
# e=a[::-1]
# f=e.replace("",",")
# print(f)



# a = "abcdefghijklmnopqrstuvwxyz"
# c=a.replace("",",")
# print(c)
# d=a.replace("","|")
# print(d)
# e=a[::-1]
# f=e.replace("",",")
# print(f)



# a = "abcdefghijklmnopqrstuvwxyz"
# c=a.replace("",",")
# print(c)
# d=a.replace("","|")
# print(d)
# e=a[::-1]
# f=e.replace("",",")
# print(f)

# a= "sa30"
# b=a.isalnum()
# print(b)


# a = "Hello " 
# b = "world"
# c=a+b
# print(c)

# a = '23.51'  
# b = 44.49
# c=int(a)
# print(c)


# a = "Me and You"
# c='and ' in a
# print(c)


# s = "I am 30 and 40 is my elder b10ther1."
# w=int(s[5:7])
# x=int(s[12:14])
# y=int(s[28:30])
# z=int(s[-2])
# c=w+x+y+z
# print(c)

# for s in range(1,101):
#     if s%2==0:
#         print(-s,end=",")
# print()



# a=int(input("enter your starting prime number:"))
# b=int(input("entre your ending prime number:"))
# for s in range(a,b):
#     c=2
#     while c<s:
#         if s%c==0:
#             break
#         c+=1
#     else:
#         print(s)
# print('this is all prime numbers between your startin and ending prime number.')

# a=(input("enter your numbers:"))
# b=a.split(" ")
# c=int(b[0])
# d=int(b[1])
# e=int(b[2])tis
# for s in range(1,11):
#     g=c*s
#     f=d*s
#     h=e*s
#     print(g ,"|",f ,"|",h)



# a=[45,4,65,64,64,95,67,76,78,70,5,80,90]
# b=0
# for s in range(len(a)):
#     if a[s]>b:
#         b=a[s]
#     if a[s]<b:
#         print(a[s])



# a=["pratik","tikaram","satish","munna"]
# b=[50,75,90,102]
# for s in range(len(a)):
#     print(a[s],":"+str(b[s]))



# a=int(input("ennter your number :"))
# b=a%1000
# f=a//1000
# c=b//100
# e=b%100
# print(str(f)+str(e)+str(c))



############## fibonacci series till 100 #############################
# x=1
# y=1
# z=0
# while z<100:
#     print(z,end=",")
#     x=y
#     y=z
#     z=x+y
print()
#######################################################################
# 2. Fibonacci series with input.
# INPUT: 12
# OUTPUT: 144
# i=int(input("enter your number :"))
# x=1
# y=1
# z=0
# a=0
# while True:
#     a+=1
#     x=y
#     y=z
#     z=x+y
#     if a==i:
#         print(z)
#         break

# ########################### 3. Check if it`s Fibonacci numbers.#############
# i=int(input("enter number :-- "))
# a=0
# b=1
# c=0
# while c<i:
#     a=b
#     b=c
#     c=a+b
# if c==i:
#     print("yes")
# else:
#     print("no")

# ################## 4. Given two integers n and k. Find position the n\’th multiple of K in the Fibonacci series.############
# a=int(input("enter your multpul :"))
# b=int(input("enter your number :"))
# c=0
# x=1
# y=1
# z=0
# count=0
# while True:
#     count+=1
#     x=y
#     y=z
#     z=x+y
#     if z%a==0:
#         c+=1
#     if c==b:
#         break
# print(count)


################## find maximum number Without using short ##############################
# a=[45,4,65,64,64,95,67,345,76,78,70,5,80,90,100]
# b=0
# for s in a:
#     if s>b:
#         b=s
# print(b)

################# find minimum number without using short ##################################
# a=[45,4,65,64,64,95,67,76,78,70,5,80,90]
# c=a[0]
# for s in a:
#     if s<c:
#         c=s
# print(c)

# a=[12,13,90,48,70,43,7]
# hn=a[0]
# for i in a:
#     if hn > i:
#         hn=i
# print(hn)

i=int(input("enter number :-"))
a=0
b=1
c=0
while a<=i:
    print(c)
    a=b
    b=c
    c=a+b
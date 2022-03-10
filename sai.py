# meraki Que
# Que 0
# a=0
# while a<=100:
#     print(a)
#     a+=1




# Que 1

# a=0
# sum=0
# while a<=100:
#     if a%7==0 and a%5==0:
#         sum+=a

#     a+=1
# print(sum)



# Que 2
 
# a=0
# b=0
# while a<=100:
#     b+=a
#     a+=1
# print(b)


# Que 3

# c=0
# a=1
# while a<=10:
#     b=int(input("enter your number :"))
#     c+=b
#     a+=1
# print(c)


# Que 4

# a=1
# while a<=100:
#     if a%2==0:
#         print(-a)
#     else:
#         print(" "+str(a))
#     a+=1


# Quetion set 2
# que 1

# a=556
# b=0
# while a<=656:
#     if a%7==0:
#         b+=7
#         print(b)
#     a+=1



# Que 2

# a=1
# while a<=100:
#     if a%3==0 and a%7==0:
#         print("Navgurukul")
#     elif a%3==0:
#         print("Nav")
#     elif a%7==0:
#         print("Gurukul")
#     else:
#         print(a)
#     a+=1


# Que 3

# a=1
# c=0
# while a<=10:
#     b=int(input("enter your number :"))
#     c+=b
#     a+=1
# print(str(c)+"  this is total sum of your enterd numbers ")
    

# Que 4

# a=156
# b=0
# while a>=147:
#     b+=1
#     print(b)
#     a-=1

# Que 5

# a=int(input("enter how much number you have add : "))
# b=1
# d=0
# while b<=a:
#     c=int(input("enter your number :"))
#     d+=c
#     b+=1
# print("SUM :"+str(d))


# # Que 6 this is code to print prime number from 1 to 100. 
# a=2
# while a<=100:
#     b=2
#     while b<a:
#         if a%b==0:
#             break
#         b+=1
#     else:
#         print(a)   
#     a+=1



# this is code to check this is prime number or composite number

# a=int(input("enter yor number :"))
# counter=0
# b=1
# while b<=a:
#     if a%b==0:
#         counter+=1
#     b+=1
# if counter==2:
#     print("this is your prime number .")
# else:
#     print("this is your composite number .")


# # Print this pattern.
# 5 5 5 5 5
# 4 4 4 4 4
# 3 3 3 3 3
# 2 2 2 2 2
# 1 1 1 1 1

# a=5
# while a>=1:
#     print(f'{str(a)} '*5)
#     a-=1


# Que set  3  

# # Que 1
# a=20
# while a<100:
#     if a%2==0:
#         print(a)
#     a+=1


# # Que 2

# a=1
# while a<100:
#     if a%7==0:
#         print(a)
#     a+=1

# Que 3

# a=12
# b=0
# while a<421:
#     b+=a
#     a+=1
# print(b)


# Que 4

# a=30
# b=0
# while a<=420:
#     if a%8==0:
#         b+=a
#     a+=1
# print(b)


# Que 5

# a=1
# c=0
# v=int(input("how much pepole yoou are :"))
# while a<=v:
#     b=int(input("enter your weight:"))
#     c+=b
#     e=c/v
#     a+=1
# print(e,"this is your average weight .")
# if e%5==0:
#     print('your average weight is multiple of 5')


# Que 7
# # guessing game

# a=int(input('enter your nmber :'))
# print("give your device to guess your number.")
# b=1
# while b<=5:
#     c=int(input("enter your guessed number :"))
#     if b==4:
#         print("this is your last chance.")
#         e=int(input("enter your guessed number :"))
#     elif c!=a:
#         print("your guessed number is not currect , try again.")
#     elif c==a :
#         print("conratulation ! your guessed number is currect.")
#         break
#     elif  e==a:
#         print("conratulation ! your guessed number is currect.")
#         break
#     else:
#         print("your all guesed number is worng , so you are out of game.")
#     b+=1



# # Que 8

# a=1
# b=int(input("enter your number :"))
# print("give your device others to guess your number. ")
# while a<=5:
#     if a==5:
#         print("this is your last chance.")
#     c=int(input("enter your guessed number :"))
#     if c<b:
#         print("your guessed number is smaller.")
#     elif c>b:
#         print('your guessed number is greater .')
#     elif c==b:
#         print("congrats ! your guessed number is currect.")
#         break
#     else:
#         print("your all guesses is wrong , your are out of game.")
#     a+=1


# Que 9

# a=int(input("enter your number :"))
# b=int(input("enter your second number :"))
# c=1
# d=0
# while c<=b:
#     d+=a
#     c+=1
# print(d,"this is multiplication of your numbers.")

# Que 10 febonnaci seares

# x=0
# y=1
# z=0
# while x<=100:
#     print(z) 
#     x=y
#     y=z
#     z=x+y
#     x+=1



# for loop
# Que 1

# for i in range(1,101):
#     print(i)


# Que 2

# for i in range(7,100,7):
#     print(i)


# Que 3

# b=0
# for i in range(100):
#     b+=i
# print(b)


# # Que 4
# b=0
# for i in range(10):
#     a=int(input("enter your number :"))
#     b+=a
# print(b,"this is sum of your numbers . ")


# Que 5

# for s in range(1,101):
#     if s%2==0:
#         print(-s)
#     else:
#         print("",s)


# Que set 2
# Que 1

# a=0
# for s in range(556,656):
#     a+=1
#     if a%7==0:
#         print(a)

# Que 2
# for s in range(1,100):
#     if s%7==0 and s%3==0:
#         print("NavGurukul")
#     elif s%3==0:
#         print("Nav")
#     elif s%7==0:
#         print("Gurukul")
#     else:
#         print(s)


# # Que 3
# a=0
# for i in range(10):
#     b=int(input("enter your number :"))
#     a+=b
# print(a,"this is the sum of your numbers.")


# Que 4
# a=1
# for s in range(156,166):
#     print(a)
#     a+=1


# # Que 5
# c=0
# a=int(input("enter how much number you : "))
# for s in range(a):
#     b=int(input("enter your number:"))
#     c+=b
# print(c,"this is somin1 = input("Enter Name: ")
# in2 = input("Remove: ")
# in3 = input("Nearwal: ")
# newstr = ""
# old = ""
# new = ""
# counter = 0
# l = len(in1)
# while counter<l:
#     print(in1[counter])
#     if counter+1<l:
#         new = in1[counter+1]
#     else:
#         new = ""
#     if counter != 0:
#         old = in1[counter-1]
#     else:
#         old = ""
#     if in1[counter]==in2 and (new==in3 or old == in3):
#         print("ye hai")
#     else:
#         newstr+=in1[counter]
#     counter+=1
# print(newstr)


# ### run for loop infinite
# s = [1]
# for i in s:
#     print(i)
#     s.append(i+1)e of your all numbers.")


# Que 6 prime numbers
# for s in range(101):
#     b=2
#     while b<s:
#         if s%b==0:
#             break
#         b+=1
#     else:
#         print(b)
    


# Que 7
# for s in range(5):
#     b=5-s
#     print(f'{(str(b))} '*5)


# Quetion set 3

# Que 1
# for s in range (20,100,2):
#     print(s)

# Que 2
# for s in range(7,100,7):
#     print(s)


# Que 3
# a=0
# for s in range(12,421):
#     a+=s
# print(a,"this is the sum of all numbers from 12 to 421")


# Que 4
# a=0
# for s in range(30,420):
#     if s%8==0:
#         a+=s
# print(a)


# Que 5
# c=0
# a=int(input("how much pepole you are:"))
# for s in range(a):
#     b=int(input("enter your weight :"))
#     c+=b
#     d=c/a
# print(d,"this is your average weight : ")
# if d%5==0:
#     print("your average weight is multile of 5 ")


# Que 6
# for s in range(100):
#     if s%2==0:
#         print(-s)
#     else:
#         print("",s)

# Que 7
# m=int(input("enter your number :"))
# print("give your device others to guess your number .")
# for s in range(5):
#     if s==4:
#         print("this is your last chance :")
#     a=int(input("enter your guessed number:"))
#     if a>m:
#         print('your gussed number is greater.')
#     elif a<m:
#         print("your gussed number is smaller.")
#     elif a==m:
#         print("congrats! your guessed number is currect.")
#         break
#     else:
#         print("your all guessed number is wong so , you are are out of game.")


# Que 9
# a=int(input("enter your number :"))
# b=int(input('enter your second number:'))
# c=0
# for s in range (a):
#     c+=b
# print(c,"this is sum of your multiplication of your numbers.")



# Que 10
# z=0
# x=0
# y=1
# for  s in range(12):
#     print(z)
#     x=y
#     y=z
#     z=x+y
#     x+=1

    
# a=(input("enter your numbers :"))
# print((a[-3]),a([-2]))

# extra Quetion given by sai. 13/9/21
# # Que 1 to make table from one to input
# c=1
# b=1
# a=int(input("up to how much your need number tables :"))
# while c<=a:
#     while b<=10:
#         print(c,"x",b,"=",b*c)
#         if b==10:
#             b=0
#             print()
#         if b==0:
#              c+=1
#              if c>a:
#                 break
#         b+=1
    

# Que 2

# a=int(input("up to how much your need factorial :"))
# b=a
# c=0
# while b!=0:
#     c*=b
#     print(c)
#     b-=1



# progrece traking of 15 sept
# Que 1

# a=input("enter a name :")
# b=input("enter a symbol:")
# c=0
# e=""
# while c<len(a):
#     d=a[c]+b
#     e+=d
#     c+=1
# print(e[0:-1])


# Que 2



# c=a
# while 1<=c:
#     if a%c==0 and b%c==0:
#         print(c)
#         break
#     c-=1

# a=int(input("enter a number :"))
# b=int(input("enter your second number:"))
# c=1
# e=[]
# if a>b:
#     d=a
# elif b>a:
#     d=b
# while c<d:
#     if a%c==0 and b%c==0:
#         f=c
#     c+=1
# print(f,"this is your greates common divisor.")



# Que 3

# b=int(input("enter number:"))
# i=1
# while i<=b:
#     j=i
#     c=1
#     while j!=0:
#         c*=j
#         j-=1
#     print(str(i)+"!","=",c)
#     i+=1
# print("this all is factorials.")

# Que 4 
# Division of string

# a=(input("enter name :"))
# b=len(a)//2
# c=a[:b]
# d=a[b:]
# print(c)
# print(d)



# Questions of 19.9.2021
# # pattern print
# a=int(input("enter number :"))
# for s in range(1,a+1):
#     print(f'{str(s)} '*s)



# take int input from user and print the -3 and -2 positions number 

# n=int(input("enter your number :"))
# n=n//10
# n=n%100
# print(n)



# # take int input and print the sume of that of the digits

# a=int(input("enter number:"))
# c=0
# while a>0:
#     b=a%10
#     a=a//10
# #     c+=b
# # print(c)
#     print(b)




# print odd even number horizontaly

# odd = ""
# even = ""
# for i in range(20):
#     if i%2==0:
#         even+=f" {i}"
#     else:
#         odd += f" {i}"
# print(odd)
# print(even)


# # print odd even number verticaly first odd numbers after that even

# odd = ""
# even = ""
# for i in range(20):
#     if i%2==0:
#         even+=f" {i}\n"
#     else:
#         odd += f" {i}\n"
# print(odd)
# print(even)


# 20.9.2021

# print the length of string without using len function

# s=input("ente your name :")
# a=s.find(s[-1])+1
# print(a)

# b=s.rindex(s[-1])+1
# print(b)


# c=0
# for i in s:
#     c+=1
# print(c)


# 21.9.2021
### UNIVERSAL CODE FROM THE USER INPUT ###
### FIBONACCI NUMBERS
### ARMSTRONG NUMBERS
### HARSHAD NUMBERS
### STRONG NUMBERS
### HAPPY NUMBERS
### PERFECT NUMBERS


# ### FIBONACCI NUMBERS

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


### ARMSTRONG NUMBERS

# d=1
# Counter=0
# a=int(input("up to how much you need amstrong numbers :"))
# while a>=d:
#     e=d
#     c=0
#     while e>0:
#         b=e%10
#         e=e//10
#         c+=b**3
#     if c==d:
#         print(c)
#         Counter+=1
#     d+=1
# print("there is ",Counter,"Amstrong numburs betwee 1 to",a)

## HARSHAD NUMBERS
# a=int(input("up to how much you need Harshad numbers :"))
# s=0
# for i in range(1,a+1):
#     st = str(i)
#     total = 0
#     for j in st:
#         total+=int(j)
#     if i/total == i//total:
#         print(i)
# print("from 1 to",a,"there is",s,"Harshad numbers that is given above.")

# # ### HAPPY NUMBERS

# for a in range(1,int(input("Enter Num:"))):
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
#             break
#         if a == 4:
#             break



### PERFECT NUMBERS

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



#### odd even number by using one loop
# a=1
# while a<20:
#     print(a)
#     a+=2
#     if a==19:
#         a=2


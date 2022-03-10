### 1) Print Odd Evern Numbers Horizontaly

# odd=""
# even=""
# a=int(input("enter your number :"))
# for s in range(1,a+1):
#     if s%2==0:
#         even+=f" {s}"
#     else :
#         s%2!=0
#         odd+=f" {s}"
# print("odd :",odd)
# print('even :',even)


### ii) Print Odd Evern Numbers Verticaly

# a=int(input("enter your number :"))
# odd = ""
# even = ""
# for i in range(1,a+1):
#     if i%2==0:
#         even+=f" {i}\n"
#     else:
#         odd += f" {i}\n"
# print("odd\n",odd)
# print("even\n",even)



### 2) Pattern printing
# 
# a=int(input("enter number :"))
# while a>0:
#     print("* "*a)
#     a=a-1
 

### 3) Strin palidrom 

# a=input("enter your name :")
# if a[::-1]==a:
#     print("this is pelindrome")
# else:
#     print("this is not pelidrome")


### ii) Int palindrom

# s=int(input("enter number:"))
# c=""
# a=s
# while a>0:
#     b=a%10
#     a=a//10
#     c+=str(b)
# if str(s)==c:
#     print('this is palindrome.')
# else:
#     print("this is not pelindrome.")
 


### 4) Annegram

# a=input("enter your latters :")
# b=input("enter your latters :")
# if len(a)==len(b):
#     for s in a:
#         print(s)
#         if s not in b:
#             print("Not annegram")
#             break
#     else:
#         print("This is annegram")
# else:
#     print("Not annegram")



### 5) Harshad Number

# a=int(input("enter your number :"))
# b=0
# for i in range(1,a+1):
#     st = str(i)
#     total = 0
#     for j in st:
#         total+=int(j)
#     if i/total == i//total:
#         b+=1
#         print(i)
# print("This is",b,"Harshad number between 1 to",a,".")


# n=int(input('Enter a number from 1 to:-'))
# for i in range(1,n+1):
#     sum=0
#     h=i
#     while i>0:
#         r=i%10
#         sum+=r
#         i=i//10
#     if h%sum==1:
#         print(h,'is harshad number')
    
# b=0
# s=int(input("enter your number :"))
# b=s**2
# f=0
# c=b%10
# d=b//10
# print(d,c)

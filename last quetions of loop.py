########### prime numbers with one loop  ############
# s=int(input("enter your aber :"))
# a=1
# b=1
# c=0
# while a<s:
#     if a%b==0:
#         c+=1
#     if b>a:
#         if c==2:
#             print(b)
#         b=1
#         c=0
#         a+=1
#     else:
#         b+=1
# print("this is your all prime abers from 1 t0",s) 

######################## print following pattern with one loop ###############
### * 
### * * 
### * * * 
### * * * * 
### * * * * * 
### * * * * 
### * * * 
### * * 
### * 


# s=int(input("enter the peack numbers of stars :"))
# a=1
# c=0
# while True:
#     if a<=s:
#         print(" *"*a,)
#     if a>=s:
#         c+=1
#         b=s-c
#         print(" *"*b,)
#         if b==0:
#             break 
#     a+=1



############ pattern print of heart ############
# for row in range(7):
#     for col in range(7):
#         if row ==0 and col in (1,2,4,5):
#             print("*",end=" ")
#         elif row==1 and col in (0,3,6):
#             print("*",end=" ")
#         elif row==2 and col in (0,6):
#             print("*",end=" ")
#         elif row==3 and col in(1,5):
#             print("*",end=" ")
#         elif row==4 and col in(2,4):
#             print("*",end=" ")
#         elif row==5 and col==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



############# pattern print of pyramid shapes #############
###       1 
###     2 1 2 
###   3 2 1 2 3 
### 4 3 2 1 2 3 4 
##5 4 3 2 1 2 3 4 5 

# a=int(input("enter the  number rows  :"))
# for i in range(1,a+1):
#     for s in range(1,a-i+1):
#          print(" ",end=" ")
#     for t in range(i,0,-1):
#         print (t,end=" ")
#     for m in range(2,i+1):
#         print (m,end=" ")
#     print()

# ############ print forllowintg pattern #######
# #### 1 2 3 4 5 
# #### 10 9 8 7 6 
# #### 11 12 13 14 15 
# #### 20 19 18 17 16 

# a=int(input("enter number of rows :"))
# b=0
# for s in range(1,a+1):
#     for v in range (5):
#         if s%2 ==0:
#             b-=1
#         else:
#             b+=1
#         print(b,end=" ")
#     b+=4
#     if s%2 == 1:
#         b+=2
#     print()


##################### write code for following output #############
#
### RAHUL
### RAHU
### RAH
### RA
### R
### K
### KU
### KUM
### KUMA
### KUMAR

# a="RAHUL"
# c="KUMAR"
# b=len(a)
# for s in range(b):
#     print(a[:b])
#     b-=1
#     if b==0:
#         for v in range(len(c)):
#             print(c[:v+1])



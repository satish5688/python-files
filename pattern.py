# ## 1) solid squear
# a=int(input("enter :"))
# for s in range(1,a+1):
#     print('*  '*a)


# ## 2) right angle triangle of stars 
# a=int(input("enter number :"))
# for s in range(1,a+1):
#     print("*"*s)

# ## left angle triagle 
# a=int(input("enter your number :"))
# for s in range(1,a+1):
#     b=a-s
#     c=b*" "
#     print(c,s*"*")


## right angle triangle
# a=int(input("enter number :"))
# b=1
# while b<=a:
#     print(b*"*")
#     b+=1


## left angle triagle
# a=int(input("enter a number :"))
# b=1
# while b<=a:
#     c=a-b
#     d=c*" "
#     print(d,b*"*")
#     b+=1

## 3) inverted right angle triangle
# a=int(input("enter nmber :"))
# for s in range(0,a+1):
#     b=a-s
#     print("*"*b)
#     if b==1:
#         break

# inverted left angle triagle
# a=int(input("enter your number :"))
# for s in range(0,a+1):
#     b=a-s
#     c=b*" "
#     print(s*" ",b*"*")
#     if b==1:
#         break


# a=int(input("enter your number :"))
# b=0
# while b<=a:
#     c=a-b
#     d=c*"*"
#     print(b*" ",c*"*")
#     b+=1
#     if c==1:
#         break

# # 4) full pyramid
# a=int(input("enter number :"))
# for s in range(1,a+1):
#     b=a-s
#     c=b*" "
#     print(c,s*" *")

# ### pyramid with while loop.
# a=int(input("enter your number :"))
# b=1
# while b<=a:
#     c=a-b
#     d=c*" "
#     print(d,b*" *")
#     b+=1

## 5) inverted full pyramid
# a=int(input("enter number :"))
# for s in range(a):
#     b=a-s
#     c=b*" *"
#     print(s*" ",c)
   

### inverted full pyramid with while loop.
# a=int(input("enter your number :"))
# s=0
# while s<=a:
#     b=a-s
#     c=b*" "
#     s+=1
#     print(s*" ",b*" *")
#     if b==1:
#         break
### 6) pyramid and inverted pyramid

# a=int(input("enter number :"))
# for s in range(1,a):
#     b=a-s
#     c=b*" "
#     print(c,s*" *")
#     if s==a-1:
#          for x in range(a):
#             z=a-x
#             y=z*" *"
#             print(x*" ",y)

 
### right angle triangle of numbers
# a=int(input("enter your number :"))
# for s in range(1,a+1):
#     for v in range(1,s+1):
#         print(v,end="")
#     print()


### inverted right angle triangle
# a=int(input("enter a number :"))
# for s in range(0,a+1):
#     b=a-s
#     for v in range(1,b+1):
#         print(v,end="")
#     print()
#     if b==1:
#         break


### inverted right angle triangle with for loop
# a=int(input("enter your number :"))
# b=0
# while b<=a:
#     c=a-b
#     v=1
#     while v<=c:
#         print(v,end="")
#         v+=1
#     print()
#     b+=1
#     if c==1:
#         break



### Right angle triagle of numbers different than above one 
# a=int(input("enter a number :"))
# a=int(input("enter your number :"))
# b=0
# while b<=a:
#     c=a-b
#     v=1
#     while v<=c:
#         print(v,end="")
#         v+=1
#     print()
#     b+=1
#     if c==1:
#         break

### pyramid with numbers 
# a=int(input("enter your number :"))
# for s in range(1,a+1):
#     if s%2!=0:
#         b=a-s
#         c=b*" "
#         print(c,s*f' {str(s)}')








# 2.10.2021

# ######### pattern print of A ###########


# for row in range(7):
#     for col in range(5):
#         if row in (1,2,3,4,5) and col in (0,4):
#             print("*",end=" ")
#         elif row==0 and col in (1,2,3):
#             print("*",end=" ")
#         elif row==3 and col in (1,2,3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# ################ pattern of B ##############
# for row in range(9):
#     for col in range(5):
#         if row in (0,1,2,3,4,5,6,7,8,9) and col==0:
#             print('*',end=" ")
#         elif row==0 and col in (1,2,3):
#             print("*",end=" ")
#         elif row==4 and col in (1,2,3):
#             print("*",end=" ")
#         elif row==8 and col in (1,2,3):
#             print("*",end=" ")
#         elif row in(1,2,3,5,6,7) and col==4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# ############### pattern of c ###############

# for row in range(5):
#     for col in range(5):
#         if row in (1,2,3,) and col ==0:
#             print("*",end=" ")
#         elif row==0 and col in (1,2,3):
#             print("*",end=" ")
#         elif row==4 and col in (1,2,3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# ########### pattern of D #####################

# for row in range(6):
#     for col in range(5):
#         if row in (0,1,2,3,4) and col==1:
#             print("*",end=" ")
#         elif row==0 and col in (0,1,2,3):
#             print("*",end=" ")
#         elif row==4 and col in (0,1,2,3):
#             print("*",end=" ")
#         elif row in (1,2,3) and col ==4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# ############## pattern print of E ###############

# for row in range(7):
#     for col in range(5):
#         if row in (0,1,2,3,4,5,6) and col==0:
#             print("*",end=" ")
#         elif row==0 and col in (1,2,3,4):
#             print("*",end=" ")
#         elif row==3 and col in (1,2,3,4):
#             print("*",end=" ")
#         elif row==6 and col in (1,2,3,4):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# ######### pattern print of F #############

# for row in range(7):
#     for col in range(5):
#         if row in (0,1,2,3,4,5,6) and col==0:
#             print("*",end=" ")
#         elif row==0 and col in (1,2,3,4):
#             print("*",end=" ")
#         elif row==3 and col in (1,2,3,4):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# ################### pattern print of G ############

# for row in range(5):
#     for col in range(8):
#         if row in (1,2,3,) and col ==0:
#             print("*",end=" ")
#         elif row==0 and col in (1,2,3):
#             print("*",end=" ")
#         elif row==4 and col in (1,2,3):
#             print("*",end=" ")
#         elif row in (3,4) and col==3:
#              print("*",end=" ")
#         elif row==2 and col in (2,3,4):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# ############## pattern print of H #############
# for row in range(8):
#     for col in range(6):
#         if row in (0,1,2,3,4,5,6) and col in (0,5):
#             print("*",end=' ')
#         elif row==3 and col in (1,2,3,4):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()

# ############## pattern print of I ###############
# for row in range(6):
#     for col in range(4):
#         if row in (0,1,2,3,4,5) and col==1:
#             print("*",end=' ')
#         elif row==0  and col in (0,2):
#             print("*",end=' ')
#         elif row==5 and col in (0,2):
#             print("*",end=' ')
#         else:
#             print(" ",end=" ")
#     print()

        
# ################ pattern print of J ##########
# for row in range(6):
#     for col in range(4):
#         if row in (0,1,2,3,4,5) and col==2:
#             print("*",end=' ')
#         elif row==0  and col in (1,2,3):
#             print("*",end=' ')
#         elif row==5 and col in (1,2):
#             print("*",end=' ')
#         elif row==4 and col==0:
#             print("*",end=' ')
#         else:
#             print(" ",end=" ")
#     print()

# ############## pattern print of K ############
# for row in range(8):
#     for col in range(7):
#         if row in (0,1,2,3,4,5,6) and col==0:
#             print("*",end=' ')
#         elif row==0 and col==4:
#             print("*",end=' ')
#         elif row==1 and col==3:
#             print("*",end=' ')
#         elif row==2 and col==2:
#             print("*",end=' ')
#         elif row==3 and col==1:
#             print("*",end=' ')
#         elif row==4 and col==2:
#             print("*",end=' ')
#         elif row==5 and col==3:
#             print("*",end=' ')
#         elif row==6 and col==4:
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()

# ############## pattern print of L ###########
# for row in range(6):
#     for col in range(6):
#         if row in(0,1,2,3,4,5) and col==0:
#             print("*",end=' ')
#         elif row ==5 and col in (1,2,3,):
#             print("*",end=' ')
#         else:
#             print(" ",end=" ")
#     print()

# ############## pattern print of M #############

# for row in  range(7):
#     for col in range(7):
#         if row in (0,1,2,3,4,5,6) and col in (0,6):
#             print("*",end=" ")
#         elif row==1 and col==1:
#             print("*",end=" ")
#         elif row==2 and col==2:
#             print("*",end=" ")
#         elif row==3 and col==3:
#             print("*",end=" ")
#         elif row==2 and col==4:
#             print("*",end=" ")
#         elif row==1 and col==5:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# ############ pattern print of N ############

# for row in  range(7):
#     for col in range(7):
#         if row in (0,1,2,3,4,5,6) and col in (0,6):
#             print("*",end=" ")
#         elif row==1 and col==1:
#             print("*",end=" ")
#         elif row==2 and col==2:
#             print("*",end=" ")
#         elif row==3 and col==3:
#             print("*",end=" ")
#         elif row==4 and col==4:
#             print("*",end=" ")
#         elif row==5 and col==5:
#             print("*",end=" ")
#         elif row==6 and col==6:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print() 

# ################ pattern print O ##############

# for  row in range(6):
#     for col in range(5):
#         if row in (1,2,3,4) and col in (0,4):
#             print("*",end=" ")
#         elif row==0 and col in (1,2,3):
#             print("*",end=" ")
#         elif row==5 and col in (1,2,3):
#             print("*",end=" ")
#         else:
#              print(" ",end=" ")
#     print()


# ############### pattern print of P #################

# for row in range(8):
#     for col in range(7):
#         if row in (0,1,2,3,4,5,6,7) and col==0:
#             print("*",end=' ')
#         elif row==0 and col in (1,2,3):
#             print("*",end=' ')
#         elif row in (1,2,3) and col==4:
#             print("*",end=' ')
#         elif row==4 and col in (1,2,3):
#             print("*",end=' ')
#         else:
#             print(" ",end=" ")
#     print()

# ############ pattern print of Q ###################

# for  row in range(8):
#     for col in range(6):
#         if row in (1,2,3,4) and col in (0,4):
#             print("*",end=" ")
#         elif row==0 and col in (1,2,3):
#             print("*",end=" ")
#         elif row==5 and col in (1,2,3,4):
#             print("*",end=" ")
#         elif row==4 and col ==3:
#             print("*",end=" ")
#         elif row==6 and col ==5:
#             print("*",end=" ")
#         else:
#              print(" ",end=" ")
#     print()

# ############### pattern print of R ##############
# for row in range(8):
#     for col in range(7):
#         if row in (0,1,2,3,4,5,6,7) and col==0:
#             print("*",end=' ')
#         elif row==0 and col in (1,2,3):
#             print("*",end=' ')
#         elif row in (1,2,3) and col==4:
#             print("*",end=' ')
#         elif row==4 and col in (1,2,3):
#             print("*",end=' ')
#         elif row==5 and col==2:
#             print("*",end=' ')
#         elif row==6 and col==3:
#             print("*",end=' ')
#         elif row==7 and col==4:
#             print("*",end=' ')
#         else:
#             print(" ",end=" ")
#     print()

# #################### pattern print of S ############

# for row in range(7):
#     for col in range(5):
#         if row in (1,2) and col==0:
#             print("*",end=" ")
#         elif row in (4,5,) and col==4:
#             print("*",end=" ")
#         elif row==0 and col in (1,2,3,4):
#             print("*",end=" ")
#         elif row==3 and col in (1,2,3):
#             print("*",end=" ")
#         elif row==6 and col in (0,1,2,3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# #################### pattern printing of T #######################
# for row in range(6):
#     for col in range(7):
#         if row in (0,1,2,3,4,5) and col==3:
#             print("*",end=" ")
#         elif row==0 and col in (0,1,2,3,4,5,6):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# ################# pattern print of U ##############
# for row in range(8):
#     for col in range(7):
#         if row in (2,3,4,5) and col in (0,4):
#             print("*",end=" ")
#         elif row==6 and col in (1,2,3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# ############### pattern print of V ###############

# for row in range(7):
#     for col in range(14):
#         if row==1 and col==1:
#             print("*",end=" ")
#         elif row==2 and col==2:
#             print("*",end=" ")
#         elif row==3 and col==3:
#             print("*",end=" ")
#         elif row==4 and col==4:
#             print("*",end=" ")
#         elif row==5 and col==5:
#             print("*",end=" ")
#         elif row==6 and col==6:
#             print("*",end=" ")
#         elif row==5 and col==7:
#             print("*",end=" ")
#         elif row==4 and col==8:
#             print("*",end=" ")
#         elif row==3 and col==9:
#             print("*",end=" ")
#         elif row==2 and col==10:
#             print("*",end=" ")
#         elif row==1 and col==11:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# ##################### PATTERN PRINT OF W ####################
# for row in range(7):
#     for col in range(7):
#         if row in (0,1,2,3,4,5,6) and col in (0,6):
#             print("*",end=" ")
#         elif row==5 and col in(1,5):
#              print("*",end=" ")
#         elif row==4 and col in(2,4):
#              print("*",end=" ")
#         elif row==3 and col==3:
#              print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# ################ pattern print of X ######################
# for row in  range(7):
#     for col in range(7):
#         if row==1 and col==1:
#             print("*",end=" ")
#         elif row==2 and col==2:
#             print("*",end=" ")
#         elif row==3 and col==3:
#             print("*",end=" ")
#         elif row==2 and col==4:
#             print("*",end=" ")
#         elif row==1 and col==5:
#             print("*",end=" ")
#         elif row==4 and col==2:
#             print("*",end=" ")
#         elif row==5 and col==1:
#             print("*",end=" ")
#         elif row==4 and col==4:
#             print("*",end=" ")
#         elif row==5 and col==5:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# ################## pattern print of Y ######################
# for row in  range(7):
#     for col in range(7):
#         if row==1 and col==1:
#             print("*",end=" ")
#         elif row==2 and col==2:
#             print("*",end=" ")
#         elif row==3 and col==3:
#             print("*",end=" ")
#         elif row==2 and col==4:
#             print("*",end=" ")
#         elif row==1 and col==5:
#             print("*",end=" ")
#         elif row in (4,5,6) and col==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# ############# pattern print of Z #################
# for row in range(7):
#     for col in range(7):
#         if row in (0,6) and col in (0,1,2,3,4,5,6):
#             print("*",end=" ")
#         elif row==1 and col==5:
#             print("*",end=" ")
#         elif row==2 and col==4:
#             print("*",end=" ")
#         elif row==3 and col==3:
#             print("*",end=" ")
#         elif row==4 and col==2:
#             print("*",end=" ")
#         elif row==5 and col==1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

##################### pattern print of circle #################

for s in range(25):
    for v in range(50):
        if s==0 and v in (23,24,25,26,27):
            print("*",end=" ")
        elif s==1 and  v in (22,28):
            print("*",end=" ")
        elif s==2 and  v in (22,24,26,28):
            print("*",end=" ")
        elif s == (3) and  v in (22,28):
            print("*",end=" ")
        elif s ==(4) and  v in (23,25,27):
            print("*",end=" ")
        elif s == (5) and  v in (24,25,26):
            print("*",end=" ")
        elif s in (6,) and   v in (24,25,26):
            print("*",end=" ")
        elif s in (7,) and   v in (22,28) :
            print("*",end=" ")
        elif s in (8,) and   v in (21,25,29) :
            print("*",end=" ")
        elif s in (9,) and   v in (20,25,30) :
            print("*",end=" ")
        elif s in (10,) and   v in (19,25,31) :
            print("*",end=" ")
        elif s in (11,) and   v in (18,25,32) :
            print("*",end=" ")
        elif s in (12,13,14,15) and   v in (25,) :
            print("*",end=" ")
        elif s in (16,) and   v in (24,26) :
            print("*",end=" ")
        elif s in (17,) and   v in (23,27) :
            print("*",end=" ")
        elif s in (18,) and   v in (22,28) :
            print("*",end=" ")
        elif s in (19,) and   v in (21,29) :
            print("*",end=" ")
        elif s in (20,) and   v in (20,30) :
            print("*",end=" ")
        elif s in (21,) and   v in (19,31) :
            print("*",end=" ")
        
        
        
        
            
            
        else:
            print(" ",end=" ")
    print()
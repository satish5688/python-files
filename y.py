# in1 = input("Enter Name: ")
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
#     s.append(i+1)



# a=int(input("eneter your number :"))
# for s in range(2,a+1):
#     b=2
#     while b<s:
#         if s%b==0:
#             break
#         b+=1
#     else:
#         print(b,end=",")
# print()




# d=1
# Counter=0
# a=int(input("up to how much you need amstrong numbers :"))
# while a>=d:
#     e=d
#     c=0
#     while e>0:
#         b=e%10
#         e=e//10
#         for i in range(1,e+1):
#     j=i

#     s=1
#     while j!=0:
#         s*=j
#         j-=1
#     # print(str(i)+"!","=",s)
#     i+=1
# # print("this all is factorials.")

#         c+=b
#     if c==d:
#         print(c)
#         Counter+=1
#     d+=1
# print("there is ",Counter,"Amstrong numburs betwee 1 to",a)





# a=int(input("enter your number :"))
# while a>0:
#     b=a%10
#     a=a//10
#     print(b)


# a=int(input('enter your number :'))
# for s in range(1,a+1):
    # c=s
    # b=1
    # while c>0:
    #     b*=c
    #     c-=1
    # print(b)



# a=int(input("enter your number :"))
# for s in range(10,a+1):
#     y=s
#     w=1
#     while y>0:
#         x=y%10
#         y=y//10
#         print(x)
#     print() 
#     while True:
#         c=x
#         b=1
#         while c>0:
#             b*=c
#             c-=1
#         print(b)
# a=1
# dd=int(input("enter your number :"  ))
# while a<=dd:
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



#### run for loop infinite 
# s=[1]
# for v in s:
#     print(v)
#     s.append(v+1)

##### print prime numbers 
# a=int(input("enter your number:"))
# for s in range(2,a+1):
#     b=2
#     while s>b:
#         if s%b==0:
#             break
#         b+=1
#     else:
#         print(b)




a=[1,2,3]
b=[2,1,4]
c=[]
# for s in a:
#     if s not in b:
#         c.append(s)
# for v in b:
#     if v not in a:
#         c.append(v)
# print(c)


for s in b:
    if s not in a:
        # print(s)
        b.append(s)
        if s in b:
            break
for v in b:
    if b.count(v)>1:
        b.remove(v)
print(b)
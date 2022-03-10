# a="im > 10 and im < 20."
# b=a[5:8]
# c=a[-3:-1]
# print(int(b)+int(c))
 

# a=1
# d=""
# while a<21:
#     b=21
#     c=b-a
#     # d+=c
#     print(c,end=",")
#     a+=1
# print()



# a=int(input('enter your number : '))
# if a<0:
#     print(-a)
# else:
#     print(a)


# a="rahul saryam"
# b=a.replace("u","p") 
# c=a.replace("y","s")
# d=c.lstrip('rahul')
# e=b.rstrip("saryam")
# print(e+" "+d)

# Quetion of loop
# Que 1


# a=1
# while a<=100:
#     print(a)
#     a+=1

# Que 2



# A=0
# a='satyam'
# b="kumar "
# c=""
# while A<len(a):
#     c+=a[A]+b[A]
#     # print(c,end="")
#     A+=1
# print(c)


# a=
# while a<=20:
#     if a%2==0:
#         print(a)
#     elif a%2!=0:
#         print(a)
#     a+=1




# a="satyam"
# b="kumar"
# c=0
# for s in range(6):
#     c+=a[s]+b[s]
#     # print(c,end="")




# msg = ' '.join(['There', 'are', 'three', 'eagles', 'in', 'the', 'sky'])
# print(msg)



# s1 = "and old"
# s2 = " falcon"

# s3 = s1.__add__(s2)
# print(s3)


# a="satyam"
# b="kumar"
# c=0
# while c<=len(a):
#     d=a[c].__add__(b)
#     print(d)
#     c+=1
# s=0
# c=0
# a=input("enter number:")
# while s<len(a):
#     b=int(a)
#     s+=1
# print

# d=0
# s=0
# a=input("enter your name:")
# b=a.split(" ")
# while s<(len(b)):
#     c=b[s]
#     d+=int(c)
#     s+=1
# print(d)



# # l='['s','a','t']'#loop 
# a=0
# f=""
# l="[1,2,3,4]"#string

# b="[,]"
# # print(len(b))
# for i in l:
#     if i in b:
#         continue
#     else:
#         f+=i
# print(type(f))
# print(f)
# b=l.find("1")
# c=l.find("2")
# d=l.find("3")
# e=l.find("4")

# a=""
# for x in l:
#     if len(x)==2:
#         pass
#     elif ","==x:
#         pass
#     elif "["==x:
#         pass
#     elif "]"==x:
#         pass
#     else:
#         a+=x
# print(a)

        
# while a<len(l):
#     if a!=2:
#         s=l[a]
#         f+=s
#         a+=1
#     print(f)


# a="  sf ffs suraj bhai"
# b=a.split()
# c=a.lstrip("sf")
# print(c)


# import requests, json


# req=requests.get("https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/golf-code")
# print((req.content))


# in1 = input("Enter Name: ")
# in2 = input("Remove: ")
# in3 = input("Nearwal: ")
# newstr = ""
# old = ""
# new = ""
# counter = 0
# l = len(in1)
# while counter<l:
#     # print(in1[counter])
#     if counter+1<l:
#         new = in1[counter+1]
#     else:
#         new = ""
#     if counter != 0:
#         old = in1[counter-1]
#     else:
#         old = ""
#     if in1[counter]==in2 and (new==in3 or old == in3):
#         # print("ye hai")
#         pass
#     else:
#         newstr+=in1[counter]
#     counter+=1
# print(newstr)



# def product(arra):
#     prod=1
#     for s in arra:
#         for v in s:
#             prod*=v
#     return prod
# print(product([[5, 1], [0.2, 4, 0.5], [3, 9]]))



import requests
from bs4 import BeautifulSoup


resp=requests.get("https://engineering.careers360.com/colleges/list-of-top-iit-colleges-in-india")
soup=BeautifulSoup(resp.content,"html.parser")
main=soup.find_all('div',class_="cardBlk").text
# maine=main.find_all('h2',class_="blockHeading")
print((main))
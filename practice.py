# s=int(input("enter any number :"))
# if s<10:
#     print("your number is less than 10")
# elif s>10 and s<20:
#     print("your number is less than 20 ")
# else:
#     print("youur number is greater than 20")


    
#  second que.

# varx = 300 - 123
# b=int(input("enter any number :"))
# if b==varx:
#     print("equal")
# else:
#     print("not equal")


# thrid que.

# number= 44 * 30
# b=int(input("enter any nmber :"))
# if b>=number:
#     print("your number is geater or equal")
# else:
#     print("your number is smaller ")



# fourth que.

# v=int(input("how much water you have in your water tank :")
# if v<1:
#     print("put more water in tank")
# elif v>1 and v<10:
#     print("there is no need of water ")
# else:
#     print("sayya ne deha aise i mai pani pani ho gai")



# que 5

# a=int(input("enter any number :"))
# if a%2==0:
#     print("your number is divisible by 2")
# else :
#     print("not divisible by 2")    


# que 6

# a=int(input("enter any number :"))
# b=int(input("enter another number :"))
# if a%b==0:
#     print("your frits no. is divisible by second ")
# else:
#     print("not divisible")



# que 7

# a=int(input("enter any number :"))
# b=int(input("enter another number :"))
# if a>b:
#     print("your greater number is "+str(a))
# elif b>a:
#     print("your grater  number is "+str(b))



# que 8

# a=int(input('enter any number :'))
# if a%5==0 and a%15==0:
#     print("your number is divisible by 5 and 15 both")
# elif a%5==0 or a%15==0:
#     print("your number is divisible by ither 5 or 15 but not by both")
# else :
#     print("your no. is not divisible by 5 and 15 ")


# que 9

# a=int(input("enter your age :"))
# if a>=5:
#     print("you can go to school ")
# if a>=18:
#     print("you can vote in election ")
# if a>=21:
#     print('you can drive car ')
# if a>=25:
#     print("you can do marrage and you can do what ever you want ")



# a=int(input("enter speed of your car :"))
# if a<=30:
#     print("speed bahot kam hai")
# elif a<=60:
#     print("speed kam hai")
# elif a>=100:
#     print("speed bahot jyada hai.")


# day = input("Aaj ka din kya hai? (monday/tuesday) > ")
# time = input("Kaunse samay ka khana banana hai? (lunch/dinner) > ")
# if day == "tuesday" and time == "dinner":
#     print ("Pav-Bhaji banegi aaj toh :)")
# elif day == "monday" or day == "tuesday":
#     print ("Daal-Roti banegi aaj")


# a=5
# b=4
# if a>b:
#     print("y")
# elif a==b:
#     print("n")
# else :
#     print("N")
# print("hello word")
# if a>=b:
#     print('Y')


# code to check greater and second greater number 

# s=int(input("enter first number :"))
# t=int(input("enter second  number :"))
# m=int(input("enter third number :"))
# if s==t and t==m :
#     print("your all three numbers are equal")
# elif s>t and s>m:
#     print(str(s)+'..this  is greater number .')
# elif t>s and t>m:
#     print(str(t)+"..this  is greater number .")
# elif m>t and m>s:
#     print(str(m)+"..this  is greater number :")
# elif s==t:
#     print("your first and second number is equal and that both is grater numbers ")
#     print(str(m)+" this is second greater munber")
# elif t==m:
#     print("your second and third number is same and that both is grater numbers")
#     print(str(s)+" this is second greater munber")

# elif m==s:
#     print("your frist and third number is equal and that both is grater numbers")
#     print(str(t)+" this is second greater munber")


# if s>t and t>m:
#     print(str(t)+" this is second greater munber")
# elif t>m and m>s:
#     print(str(m)+" this is second greater munber")
# elif m>s and s>t:
#     print(str(s)+" this is second greater munber")
# elif s>m and m>t:
#     print(str(m)+" this is second greater munber")
# elif t>s and s>m:
#     print(str(s)+" this is second greater munber")
# elif m>t and t>s:
#     print(str(t)+" this is second greater munber")
# else:
#     if s==t and s<m:
#         print(str(s)+" this is second greater munber")
#     elif t==m and s>t:
#         print(str(t)+" this is second greater munber")
#     elif s==m and t>s :
#         print(str(m)+" th.is is second greater munber")


##### 29.9.21   
### print the number table up to input.
# a=int(input("enter your number :"))
# for s in range(1,a+1):
#     for v in range(1,11):
#         print(s,"x",v,"=",s*v)
#     print()
#     print()


#### print the number table of input
# a=int(input("enter your number :"))
# for s in  range(1,11):
#     print(a*s)



#### print factorial
# a=int(input('enter your number:'))
# for s in range(1,a+1):
#     b=1
#     while s>0:
#         b*=s
#         s-=1
#     print(b)



#### print prime number 
# a=int(input("enter your number :"))
# for s in range(2,a+1):
#     b=2
#     while s>b:
#         if s%b==0:
#             break
#         b+=1
#     else:
#         print(b)



####### print the squear of the number up to input
# a=int(input("enter your number :"))
# for s  in range (1,a+1):
#     b=s**2
#     print(s,"=",b)



#### print febbonici serise
# a=int(input("enter your number :"))
# x=0
# y=1
# z=1
# while z<a:
#     print(z)
#     x=y
#     y=z
#     z=x+y

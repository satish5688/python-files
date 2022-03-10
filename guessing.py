print("*********** welcome to guessing game ************* ")
import random

a=random.randint(0,10)
print(a)
b=int(input("enter number wich you guess :"))
if b>a:
    print("your number is greater than actual number .")
elif b<a:
    print("your number is smaller than actual number.")
elif b==a:
    print(" congratulation ! your guesss number is currect.")
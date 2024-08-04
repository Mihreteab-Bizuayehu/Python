# ************* while loop ************* #

import random

# Listing a numbers between a certain range.
lists=[]
number=int(input("Enter the number you want? "))
print("#################################")
count=1
while count<=number:
    lists.append(count)
    count+=1
print("lists=",lists)

print("#################################")
print("#################################")


# Number guessing game
number=int(input("Enter the maximum number: "))
RandomNumber=random.randint(1,number)
guess=None

while guess != RandomNumber:
    guess=int(input(f"Guess a number between 1 and {number}: "))
    if guess<RandomNumber:
        print("Too low!")
    elif guess>RandomNumber:
        print("Too high!")
print(f"🎉Congratulations, you got the answer {guess}={RandomNumber}!")

print("#################################")
print("#################################")

# Fibonacci sequence using while loop.
iterator=int(input("Enter the number of iteration? "))
count=0
a,b=[0,1]
sequences=[]

while count<iterator:
    sequences.append(a)
    a,b=b,a+b
    count += 1
print(f"sequences={sequences}")


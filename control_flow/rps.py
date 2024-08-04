import random
import sys

print("========================================")
print("==========Rock, Paper and Scisor Game=========")
print("========================================")
UserChoice=input("Enter your choice\n 1 for Rock \n 2 for Scisor \n 3 for Paper \n\n")
user=int(UserChoice)
ComputerChoice=random.choice("123")
computer=int(ComputerChoice)
print("")
print("You chose" + UserChoice + ".")
print("Computer chose" + ComputerChoice + ".")

if user<1 or user>3:
    sys.exit("You must enter 1, 2 or 3.")
elif user==computer:
    print("🟰 The game  tie!")
elif user==1 and computer==2:
    print("🎉 You win!")
elif user==2 and computer==3:
    print("🎉 You win!")
elif user==3 and computer==1:
    print("🎉 You win!")
else:
    print("🐍 You lose!")
    


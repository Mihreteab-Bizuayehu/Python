# ************* for loop ************* #

# Adding the item of the numerical list.
numbers=[23,43,45,65,67,89,98,90,76,56]
total=0      
for number in numbers:
    total+=number
print("")
print(f"The sum of list items: \n Total={total}")

# Calculate the fuctorial of the number you enter.
num=int(input("Enter the number you want ? \n"))
factorials=1
if num<0:
    print("The number should be greater tha or equal to zero!")
elif num==0 or num==1:
   print(f" The factorial of:\n {num}!={factorials} ")
else:
    for i in range(2, num + 1):
        factorials *= i
    print(f" The factorial of:\n {num}!={factorials} ")
 







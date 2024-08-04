num1=float(input("Enter the first number : "))
num2=float(input("Enter the second number : "))
operator=input("Select the operator  (+,-,*,/,%,**,//): ")

if operator == "+":
    print(f"The summation of num1 and num2 is ", num1+num2)
elif operator == "-":
    print(f"The difference of num1 and num2 is ", num1 - num2)
elif operator == "*":
    print(f"The product of num1 and num2 is ", num1 * num2)
elif operator == "/":
    print(f"The division of num1 by num2 is ", num1 / num2)
elif operator == "%":
    print(f"The reminder of num1 and num2 is ", num1 % num2)
elif operator == "**":
    print(f"The result of num1 the power of num2 is ", num1 ** num2)
elif operator == "//":
    print(f"The the floor divition of num1 by num2 is ", num1 // num2)
else:
    print(" Invalid operation")
#  Built in functions are already prepared for python to access and use it easly like: print(), input(), bool(), float(), etc.

def calculator():
  num1=float(input("Please enter the first number?\t"))
  num2=float(input("Please enter the second number?\t"))
  choice=input("Enter your choice ('+', '-','*','/','%','//','**'):\t")
  if choice=="+":
    return print(f"total= {num1+num2}")
  elif choice=="-":
    return print(f"difference= {num1-num2}")
  elif choice=="*":
    return print(f"product= {num1*num2}")
  elif choice=="/":
    if num2!=0:
      return print(f"quetient= {num1/num2}")
    else:
      return print("The divisor must be different from zero.")
  elif choice=="**":
    if num1>=num2:
      return print(f"num1^num2= {num1**num2}")
    else:
      return print(f"num2^num1= {num2**num1}")
  elif choice=="//":
    if num2!=0:
      return print(f"fquetient= {num1//num2}")
    else:
      return print("The divisor must be different from zero.")
  elif choice=="%" :
    if num1>=num1:
     return print(f"num1%num2= {num1%num2}")
    else:
      return print(f"num2%num1= {num2%num1}")
calculator()

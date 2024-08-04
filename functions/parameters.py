# parameters and arguments by using user defined functions
print("#### parameters and arguments by using user defined functions ####")

# positional parameters
print("####### positional parameters ########")
def positional(a,b):
    return print(f"a= {a} , b={b} the sum of a and b is: sum={a+b} "  )
positional(12,45)


# keyword parameters
print("####### keyword parameters ########")
def keywords(name,age,profession):
    details={"First name":name,"Age":age,"Profession":profession}
    return details
result=keywords(name="Mihreteab",age=25,profession="Programmer")
print(result)


# Default Parameters
print("####### Default Parameters ########")
def default(name,profession="Programmer"):
    return print(f"I'm {name} amd my profession is {profession}.")
default(name="Mihreteab")
default(name="Mihreteab",profession="Software Developer")

# Variable length arguments
print("####### Variable length arguments ########")
def var_args(*args):
    total=0
    for item in args:
        total+=item
    return print(f"total={total}")
var_args(1,2)
var_args(1,2,3,4,5,6)
var_args(1,2,45,67,54,34)
var_args(1,2,21,23,12,98,67,6)


# Variable length keyword arguments
print("####### Variable length keyword arguments ########")
def var_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
var_kwargs(first_name="Mihreteab",last_name="Bizuayehu",age=25,profession="Programmer")

# Order of variable arguments rules: params,*args,defaulr params,**kwargs
print("##### arguments rules: params,*args,defaulr params,**kwargs #####")
def garbage(name,*args,profession="Programmer",**kwargs):
    total=0
    for key, item in kwargs.items():
        total += item
    return print(f"Name:{name} \nProfession:{profession} \nTotal={sum(args) +total}")
garbage("Mihreteab", 12,34,54,34,23, num1=78,num2=88,num3=98,num4=68,num5=58)





# ////-----Common list opperations------//// # 

# Creating a list
fruits = ["apple", "orange", "lemon", "mango", "papaya"]
newList=["temir", "penapple", "zeitun"]

# ----------Add to list----------#

# Add element to list 
fruits.append("abocado")
print(fruits)

# Add new list to prexisting list 
fruits.extend(newList)
print(fruits)

fruits.sort(reverse=True)
print(fruits)

 # ----------Access telements from list----------#

# Accessing single element using index
print(fruits[2])

# Accessing all elements using loop
for fruit in fruits:
    print(fruit, end=", ")


# ----------Remove element from list----------#
fruits.remove("mango")
print(fruits)

# Remove Element using index
fruits.pop(4)
print(fruits)

# Remove all elements
fruits.clear()
print(fruits)

# ----------List Comprehension----------#

squares=[x**2 for x in range(1,10)]
print(squares)
for square in squares:
    print(square, end=", ") 





# Simple To-Do List Application

tasks=[]

def add_task(task):
    return tasks.append(task)

def remove_task(task):
    return tasks.remove(task)

def view_task():
    result=[]
    for task in tasks:
        result.append(task)
    return result

# Add task
add_task("HTML")
add_task("CSS")
add_task("Bootstrap")
add_task("JavaScript")
add_task("jQuery")
add_task("React")
add_task("WordPress")
add_task("Node")
add_task("MongoDB")
add_task("Django")

# accessing tasks
print(f"To-Do List Application\n Tasks={view_task()}")

# Remove task
remove_task("Bootstrap")
remove_task("WordPress")

print(f"Updated To-Do List Application\n Tasks={view_task()}")



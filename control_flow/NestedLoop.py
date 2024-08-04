# Pattern printing using nested loop.
rows = 5
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()



fruits=["apple","lemon","orange","mango"]

print(fruits[3])
fruits.append("abocado")
print(fruits)
fruits.remove("lemon")
print(fruits)

squers=[x**2 for x in range(10)]
print(squers)




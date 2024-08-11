#  ////////----------Common Tuple  Operations----------//////// #

# Create tuple
from copy import copy


numbers=(1, 2, 5, 3, 4, 5, 8, 6, 7, 8, 9)

print(f"numbers={numbers}")
print(f"number_of_element={len(numbers)}")
print(f"maximum_element={max(numbers)}")
print(f"minimum_element={min(numbers)}")
print(f"numbers_sorted={sorted(numbers, reverse=True)}")
print(f"number_of_eight={numbers.count(8)}")

# Access single element
print(numbers[5])

# Access all element using loop
for number in numbers:
    print(number, end=", ")

print()

numbers_copy=copy(numbers*3)
print(f"numbers_copy={numbers_copy}")
for number in numbers_copy:
    print(number, end=", ")





# Storing geographical coordinates

def location():
    return (40.7128, 74.0060)
latitude, longitude=location()
print(f"location=({latitude}, {longitude})")
